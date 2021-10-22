from typing import Tuple, Union

from SRPN.lexer.string_types import StringTypes
from SRPN.lexer.substrings import Substring
from SRPN.tokens import command, operand, operators, token


class Tokenizer:
    _STRING_VALUE_OF_ZERO = "0"

    def read_substrings(self, substrings: Tuple[Substring, ...]) -> Tuple[token.Token, ...]:
        # I know this is an unintuitive function but I find it both funny and clean so it stays :P
        tokens = (self._convert_substring_to_token(substring) for substring in substrings)
        tokens = tuple(_token for _token in tokens if _token)
        return tokens

    @staticmethod
    def _convert_substring_to_token(substring: Substring) -> Union[token.Token, None]:
        if substring.get_string_type() == StringTypes.SPACE_CHARACTER:
            return None
        elif substring.get_string_type() == StringTypes.PLUS:
            return operators.Addition()
        elif substring.get_string_type() == StringTypes.MINUS:
            return operators.Subtraction()
        elif substring.get_string_type() == StringTypes.MULTIPLY:
            return operators.Product()
        elif substring.get_string_type() == StringTypes.DIVIDE:
            return operators.Quotient()
        elif substring.get_string_type() == StringTypes.MODULO:
            return operators.Modulo()
        elif substring.get_string_type() == StringTypes.EXPONENT:
            return operators.Exponentiation()
        elif substring.get_string_type() == StringTypes.DIGITS:
            return operand.Operand(substring.get_string())
        elif substring.get_string_type() == StringTypes.LETTER_D:
            return command.OutputStack()
        elif substring.get_string_type() == StringTypes.EQUALS:
            return command.OutputTopOfStack()
        elif substring.get_string_type() == StringTypes.HASHTAG:
            return operand.Operand(Tokenizer._STRING_VALUE_OF_ZERO)
        elif substring.get_string_type() == StringTypes.RANDOM:
            return command.StoreRandomInteger()
        elif substring.get_string_type() == StringTypes.NON_VALUE:
            return operand.Operand(Tokenizer._STRING_VALUE_OF_ZERO)
