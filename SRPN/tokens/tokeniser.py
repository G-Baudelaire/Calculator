from typing import Tuple, Union

from SRPN.lexer.string_types import StringTypes
from SRPN.lexer.substrings import Substring
from SRPN.tokens.operators import Subtraction
from SRPN.tokens.token import Token


class Tokeniser:
    def read_substrings(self, substrings: Tuple[Substring, ...]):
        tokens = list()

    @staticmethod
    def _convert_substring_to_token(substring: Substring) -> Union[Token, None]:
        SPACE_CHARACTER = 1
        PLUS = 2
        MINUS = 3
        MULTIPLY = 4
        DIVIDE = 5
        MODULUS = 6
        EXPONENT = 7
        DIGITS = 8
        LETTER_D = 9
        EQUALS = 10
        HASHTAG = 11
        NON_VALUE = 12
        if substring.get_string_type() == StringTypes.SPACE_CHARACTER:
            return None
        elif substring.get_string_type() == StringTypes.SPACE_CHARACTER:
        elif substring.get_string_type() == StringTypes.PLUS:
        elif substring.get_string_type() == StringTypes.MINUS:
        elif substring.get_string_type() == StringTypes.MULTIPLY:
        elif substring.get_string_type() == StringTypes.DIVIDE:
        elif substring.get_string_type() == StringTypes.MODULUS:
        elif substring.get_string_type() == StringTypes.EXPONENT:
        elif substring.get_string_type() == StringTypes.DIGITS:
        elif substring.get_string_type() == StringTypes.LETTER_D:
