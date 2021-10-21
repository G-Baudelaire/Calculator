class Error:
    _error_string: str

    def get_error_string(self) -> str:
        return self._error_string


class StackUnderflow(Error):
    _error_string: str = "Stack underflow."


class StackOverflow(Error):
    _error_string: str = "Stack overflow."


class DivideByZero(Error):
    _error_string: str = "Divide by 0"
