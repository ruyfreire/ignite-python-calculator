from .http_bad_request import HttpBadRequestError


def error_controller(error: Exception):
    if isinstance(error, HttpBadRequestError):
        return {
            "status_code": error.status_code,
            "body": [{
                "name": error.name,
                "detail": error.message
            }]
        }

    return {
        "status_code": 500,
        "body": [{
            "name": "Internal Server Error",
            "detail": str(error)
        }]
    }
