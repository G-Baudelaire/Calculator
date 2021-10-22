from SRPN.tokens.general_methods import GeneralMethods
from SRPN.tokens.token import Token


class Operand(Token):
    def __init__(self, string: str):
        self._value = GeneralMethods.bound_output(int(string))

    def get_value(self) -> int:
        return self._value
