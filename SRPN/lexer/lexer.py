from typing import List

from patterns import Patterns
from substrings import Substring
from string_types import StringTypes
import re


class Lexer():
    def __init__(self):
        self._comment_open = False

    def read_user_input(self, user_input: str):
        substrings = self._decompose_command(user_input)
        self._verify_minus_operands(substrings)

    def _decompose_command(self, string):
        substrings = list()

        while len(string) != 0:
            for pattern, string_type in zip(Patterns.PATTERNS_LIST, StringTypes.STRING_TYPES):
                match = re.match(pattern, string)
                if match:
                    string = string[match.end():]
                    substrings.append(Substring(match.group(), string_type))
                    break
                else:
                    continue

        return substrings

    def _verify_minus_operands(self, substrings):
        i = 0
        while i < len(substrings):
            substring = substrings[i]
            if substring.get_string_type() == StringTypes.MINUS and self._is_minus_for_operand(i, substrings):
                self._combine_minus_with_operand(i, substrings)
            i += 1

    def _combine_minus_with_operand(self, index: int, substrings: List[Substring]):
        minus_substring = substrings.pop(index)
        operand_substring = substrings.pop(index)
        new_operand = Substring(
            (minus_substring.get_string() + operand_substring.get_string()),
            operand_substring.get_string_type()
        )
        substrings.insert(index, new_operand)

    def _is_minus_for_operand(self, index, substrings: List[Substring]) -> bool:
        pointer = index
        final_index = len(substrings) - 1
        consecutive_minuses = 0

        if (index == final_index) or (substrings[index + 1].get_string_type() != StringTypes.DIGITS):
            return False

        while (0 <= pointer) and (substrings[pointer].get_string_type() == StringTypes.MINUS):
            consecutive_minuses += 1
            pointer -= 1

        odd_consecutive_minuses = bool(consecutive_minuses % 2)
        if (substrings[pointer].get_string_type() == StringTypes.DIGITS) and (0 <= pointer):
            return not odd_consecutive_minuses
        else:
            return odd_consecutive_minuses


if __name__ == '__main__':
    lexer = Lexer()
    lexer.read_user_input("1 2 -3-4 5 6 - -7 --8")
