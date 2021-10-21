"""
Substring wrapper used in the lexing process.
"""


class Substring:
    """
    Class used to store information about a substring during the lexing process.
    """

    def __str__(self) -> str:
        return self._string

    def __int__(self) -> int:
        return self._string_type

    def __init__(self, string: str, string_type: int):
        self._string = string
        self._string_type = string_type

    def get_string(self) -> str:
        """
        :return: The string value of a substring.
        """
        return self._string

    def get_string_type(self) -> int:
        """
        :return: The type of substring from a list of constants.
        """
        return self._string_type
