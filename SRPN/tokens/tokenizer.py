from typing import Tuple, Union

from SRPN.lexer.string_types import StringTypes
from SRPN.lexer.substrings import Substring
from SRPN.tokens.command import OutputStack, OutputTopOfStack
from SRPN.tokens.operators import *
from SRPN.tokens.token import Token


class Tokenizer:
    _STRING_VALUE_OF_ZERO = "0"

    def read_substrings(self, substrings: Tuple[Substring, ...]):
        tokens = [self._convert_substring_to_token(substring) for substring in substrings]
        # I know this is an unintuitive line but I find it funny so it's staying in there.
        tokens = [token for token in tokens if token]

    @staticmethod
    def _convert_substring_to_token(substring: Substring) -> Union[Token, None]:
        if substring.get_string_type() == StringTypes.SPACE_CHARACTER:
            return None
        elif substring.get_string_type() == StringTypes.PLUS:
            return Addition()
        elif substring.get_string_type() == StringTypes.MINUS:
            return Subtraction()
        elif substring.get_string_type() == StringTypes.MULTIPLY:
            return Product()
        elif substring.get_string_type() == StringTypes.DIVIDE:
            return Quotient()
        elif substring.get_string_type() == StringTypes.MODULO:
            return Modulo()
        elif substring.get_string_type() == StringTypes.EXPONENT:
            return Exponentiation()
        elif substring.get_string_type() == StringTypes.DIGITS:
            return Operand(substring.get_string())
        elif substring.get_string_type() == StringTypes.LETTER_D:
            return OutputStack()
        elif substring.get_string_type() == StringTypes.EQUALS:
            return OutputTopOfStack()
        elif substring.get_string_type() == StringTypes.HASHTAG:
            return Operand(Tokenizer._STRING_VALUE_OF_ZERO)
        elif substring.get_string_type() == StringTypes.NON_VALUE:
            return Operand(Tokenizer._STRING_VALUE_OF_ZERO)
