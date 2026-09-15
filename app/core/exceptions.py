class AppException(Exception):
    """Base class for all application exceptions."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ExternalAPIError(AppException):
    """Raised when an external API call fails."""
    pass

class ResourceNotFoundError(AppException):
    """Raised when a requested resource is not found."""
    pass
