from typing import List, Tuple

from patterns import Patterns
from substrings import Substring
from string_types import StringTypes
import re


class Lexer():
    def __init__(self):
        self._comment_open = False

    def read_user_input(self, user_input: str):
        substrings = self._decompose_command(user_input)
        print("decompose")
        print(tuple(str(i) for i in substrings))
        substrings = self._verify_hashtag_commands(substrings)
        print("remove comments")
        print(tuple(str(i) for i in substrings))
        substrings = self._verify_minus_operands(substrings)
        print("group negative operands")
        print(tuple(str(i) for i in substrings))

    def _decompose_command(self, string: str) -> Tuple[Substring, ...]:
        """
        Receive user input, break it down into substrings that are used in the algorithms to determine what are the
        separate parts of the command.
        :param string: User input.
        :return: Tuple of substring objects.
        """
        substrings = list()

        while len(string) != 0:
            for pattern, string_type in zip(Patterns.PATTERNS_LIST, StringTypes.STRING_TYPES):
                match = re.match(pattern, string)
                if match:
                    string = string[match.end():]
                    substrings.append(Substring(match.group(), string_type))
                    break

        return tuple(substrings)

    def _verify_hashtag_commands(self, substrings: Tuple[Substring, ...]) -> Tuple[Substring, ...]:
        """
        Find and remove all comments in the decomposed user input.
        :param substrings: Tuple of the decomposed user input as Substrings.
        :return: Tuple of Substrings with all comments removed.
        """
        comment_marker_indexes = list()

        for index, substring in enumerate(substrings):
            substring_type = substring.get_string_type()
            if substring_type == StringTypes.HASHTAG and self._is_hashtag_a_comment_marker(substrings, index):
                comment_marker_indexes.append(index)

        comment_marker_indexes = tuple(comment_marker_indexes)
        return self._remove_comment_substrings(substrings, comment_marker_indexes)

    def _is_hashtag_a_comment_marker(self, substrings: Tuple[Substring, ...], index) -> bool:
        """
        Check if a hashtag fufills the requirements to be read as a comment marker
        :param substrings:
        :param index:
        :return:
        """
        final_index = len(substrings) - 1

        valid_preceding_substring = bool(
            (index == 0) or (substrings[index - 1].get_string_type() == StringTypes.SPACE_CHARACTER)
        )
        valid_subsequent_substring = bool(
            (index == final_index) or (substrings[index + 1].get_string_type() == StringTypes.SPACE_CHARACTER)
        )

        return bool(valid_preceding_substring and valid_subsequent_substring)

    def _remove_comment_substrings(
            self, substrings: Tuple[Substring, ...], comment_marker_indexes: Tuple[int, ...]) -> Tuple[Substring, ...]:
        substrings = list(substrings)
        new_substrings, partitions = list(), list()

        starting_index = 0
        for index in comment_marker_indexes:
            partitions.append(substrings[starting_index: index])
            starting_index = index + 1
        partitions.append(substrings[starting_index:])

        partitions = partitions[self._comment_open::2]
        for i in partitions:
            new_substrings.extend(i)

        odd_number_of_markers = bool(len(comment_marker_indexes) % 2)
        self._comment_open = self._comment_open ^ odd_number_of_markers

        return tuple(new_substrings)

    def _verify_minus_operands(self, substrings: Tuple[Substring, ...]) -> Tuple[Substring, ...]:
        minus_operand_indexes = list()

        for index, substring in enumerate(substrings):
            substring_type = substring.get_string_type()
            if substring_type == StringTypes.MINUS and self._is_minus_for_operand(substrings, index):
                minus_operand_indexes.append(index)

        minus_operand_indexes = tuple(minus_operand_indexes)
        return self._combine_minuses_with_operands(substrings, minus_operand_indexes)

    def _combine_minuses_with_operands(
            self, substrings: Tuple[Substring, ...], minus_operand_indexes: Tuple[int, ...]) -> Tuple[Substring, ...]:
        substrings = list(substrings)

        for index in reversed(minus_operand_indexes):
            minus_substring = substrings.pop(index)
            operand_substring = substrings.pop(index)
            new_operand_string = minus_substring.get_string() + operand_substring.get_string()
            new_operand = Substring(new_operand_string, StringTypes.DIGITS)
            substrings.insert(index, new_operand)
        return tuple(substrings)

    def _is_minus_for_operand(self, substrings: Tuple[Substring, ...], index) -> bool:
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
    lexer.read_user_input("  ### #")
