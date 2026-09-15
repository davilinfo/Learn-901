# System Architecture

This document describes the architectural design and the request-response execution flow of the Blockchain & Market Status API.

## 🏗️ Design Pattern: Layered Architecture

The project employs a **Layered Architecture** (also known as N-Tier Architecture). This pattern separates the application into distinct horizontal layers, where each layer has a specific responsibility and only communicates with the layer directly below it.

### Layer Definitions

1.  **Routing Layer (Interface)**:
    - **Responsibility**: Entry point of the application. It handles HTTP protocol concerns, request validation, and response formatting.
    - **Key Components**: FastAPI routers, Pydantic request models.
2.  **Service Layer (Domain/Business Logic)**:
    - **Responsibility**: Orchestrates the business logic. It doesn't care *how* data is fetched, only *what* data is needed and how it should be transformed for the user.
    - **Key Components**: `BlockchainService`, `MarketService`.
3.  **Infrastructure Layer (Clients/Adapters)**:
    - **Responsibility**: Low-level implementation of external communications (HTTP, Database, etc.). It encapsulates the specifics of external API formats and protocols.
    - **Key Components**: `LiskClient`, `CoinGeckoClient`.
4.  **Core Layer (Cross-Cutting Concerns)**:
    - **Responsibility**: Provides shared utilities, configuration, and global error handling used across all layers.
    - **Key Components**: `Settings`, `AppException`.

---

## 📐 Application of SOLID Principles

- **Single Responsibility Principle (SRP)**: Each layer has one job. A route only handles HTTP; a service only handles logic; a client only handles I/O.
- **Open/Closed Principle (OCP)**: By using Abstract Base Classes (ABCs) for clients, the system is **open for extension** (we can add a `BitcoinClient`) but **closed for modification** (we don't need to change the `BlockchainService` to support a new client).
- **Liskov Substitution Principle (LSP)**: Any concrete implementation of `BlockchainClient` can be swapped in without breaking the service layer, as they all adhere to the same abstract contract.
- **Dependency Inversion Principle (DIP)**: High-level modules (`BlockchainService`) do not depend on low-level modules (`LiskClient`); both depend on abstractions (`BlockchainClient` interface).

---

## 🔄 Request Execution Flow: Blockchain Status

Below is the step-by-step execution flow when a user calls `GET /api/v1/blockchain/status`.

### 1. Request Entry (Routing Layer)
- **Action**: The client sends an HTTP GET request to `/api/v1/blockchain/status`.
- **Execution**: FastAPI matches the route in `app/api/v1/blockchain.py`.
- **Dependency Injection**: The `Depends(get_blockchain_service)` trigger fires. The system calls `app/api/deps.py` $\rightarrow$ `get_blockchain_service()`, which instantiates a `LiskClient` and injects it into a `BlockchainService`.

### 2. Business Logic Orchestration (Service Layer)
- **Action**: The route handler calls `await service.get_status()`.
- **Execution**: The `BlockchainService` in `app/services/blockchain_service.py` receives the call. It doesn't know it's using Lisk; it only knows it has a `BlockchainClient` interface.
- **Call**: The service calls `await self.client.get_node_info()`.

### 3. External API Communication (Infrastructure Layer)
- **Action**: The `LiskClient` in `app/clients/blockchain_client.py` executes the request.
- **Execution**:
    - Uses `httpx.AsyncClient` to send an asynchronous GET request to the configured `LISK_API_URL`.
    - **Error Handling**: If the request fails (4xx/5xx or network timeout), it catches the `httpx` exception and raises a domain-specific `ExternalAPIError`.
- **Return**: The raw JSON response from the Lisk node is returned to the service layer.

### 4. Data Transformation (Service $\rightarrow$ Routing)
- **Action**: `BlockchainService` receives the raw JSON.
- **Execution**: It wraps the raw data into a `BlockchainStatusResponse` Pydantic model to ensure type safety and structure.
- **Return**: The model is returned to the route handler.

### 5. Response Delivery (Routing Layer)
- **Action**: The route handler returns the Pydantic model.
- **Execution**: FastAPI automatically serializes the model into a JSON response with a `200 OK` status code.
- **Final Output**: The client receives the JSON body.

### 🚩 Error Path
If any step in the Infrastructure Layer raises an `ExternalAPIError`:
1. The exception bubbles up through the Service layer.
2. The **Global Exception Handler** in `app/main.py` catches it.
3. The handler maps `ExternalAPIError` to a `502 Bad Gateway` response.
4. The client receives a clean JSON error: `{"error": "ExternalAPIError", "message": "..."}`.
