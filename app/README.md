# Blockchain & Market Status Web API

A high-performance, asynchronous Python API acting as a gateway for Blockchain and Market data. This project is built with a strict adherence to **SOLID principles**, ensuring that it is maintainable, testable, and easily extensible.

## 🚀 Features

- **Health Status**: Fast check of API availability.
- **Blockchain Proxy**: Real-time node info from the Lisk network.
- **Market Proxy**: Top 10 cryptocurrency prices from CoinGecko.
- **SOLID Architecture**: 
  - **SRP**: Separate layers for Routing, Service Logic, and Infrastructure.
  - **OCP/LSP**: Client interfaces (ABCs) allow adding new data providers without changing core logic.
  - **DIP**: Dependency injection via FastAPI `Depends`.
- **Async I/O**: Powered by `httpx` and `FastAPI` for non-blocking requests.
- **Robust Error Handling**: Centralized exception mapping to HTTP status codes.

## 🛠️ Installation

### Prerequisites
- Python 3.9+
- Virtual environment (recommended)

### Setup
**Important**: This project is structured as a Python package. All commands should be run from the **root directory** (`D:\AI\Learn-901`).

1. **Clone the repository** (or navigate to the project root).
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   .\\venv\\Scripts\\activate
   # Linux/Mac
   source venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r app/requirements.txt
   ```
4. **Configure environment variables**:
   The `.env` file is located inside the `app/` folder. Ensure it contains:
   ```env
   APP_ENV=development
   LISK_API_URL=https://www.liskrestaurant.com:4443/api/node/info
   COINGECKO_API_URL=https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false
   ```

## 🏃 Running the API

**Run the server from the root directory** to ensure the `app` package is correctly resolved:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can access the interactive Swagger UI:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Endpoints Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/status` | API Health Check |
| `GET` | `/api/v1/blockchain/status` | Lisk Blockchain Node Info |
| `GET` | `/api/v1/market/prices` | Top 10 Crypto Prices (CoinGecko) |
| `GET` | `/` | Root information |

## 🏗️ Architecture Overview

```text
. (Root Directory)
└── app/
    ├── .env                    # Configuration
    ├── requirements.txt       # Dependencies
    ├── main.py                 # Entry point & Global Exception Handlers
    ├── core/                   # Config & Exceptions
    ├── api/                    # Routes & Dependency Injection
    ├── services/              # Business Logic (Domain Layer)
    ├── clients/                # External API Adapters (Infrastructure Layer)
    └── schemas/                # Pydantic Data Models
```
