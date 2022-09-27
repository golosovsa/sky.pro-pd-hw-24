"""
    Exception ServerError
"""
from werkzeug.exceptions import HTTPException


class ServerError(HTTPException):
    pass
