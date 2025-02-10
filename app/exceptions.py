from fastapi import HTTPException, status

class BaseException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)

class InvalidSignatureException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid signature"

class TransactionAlreadyExistsException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Transaction already exists"

class UserIsNotAuntificatedException(BaseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "User is not authenticated"

class InvalidTokenException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid token"

class TokenExpiredException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Token expired"

class UserIsNotPresentException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User is not present"

class BillNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Bill not found"

class InvalidPasswordOrEmailException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Invalid password or email"

class EmailAlreadyRegisteredException(BaseException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Email already registered"

class AccessDeniedException(BaseException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Access denied"

class TransactionsNotFoundException(BaseException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Transactions not found"

class AlreadyLoggedInException(BaseException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "You are already logged in"