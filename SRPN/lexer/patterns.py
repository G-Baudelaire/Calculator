"""
Constants used as regex patterns in the lexing process.
"""


class Patterns:
    """
    Class of pattern constants.
    """
    SPACE_CHARACTER_PATTERN = r" "
    PLUS_PATTERN = r"\+"
    MINUS_PATTERN = r"-"
    MULTIPLY_PATTERN = r"\*"
    DIVIDE_PATTERN = r"\/"
    MODULUS_PATTERN = r"%"
    EXPONENT_PATTERN = r"\^"
    DIGITS_PATTERN = r"\d+"
    COMMAND_D_PATTERN = r"d"
    COMMAND_EQUALS_PATTERN = r"="
    HASHTAG_PATTERN = r"#"
    COMMAND_RANDOM = r"r"
    NON_VALUE_PATTERN = r"."
    PATTERNS_LIST = [
        SPACE_CHARACTER_PATTERN,
        PLUS_PATTERN,
        MINUS_PATTERN,
        MULTIPLY_PATTERN,
        DIVIDE_PATTERN,
        MODULUS_PATTERN,
        EXPONENT_PATTERN,
        DIGITS_PATTERN,
        COMMAND_D_PATTERN,
        COMMAND_EQUALS_PATTERN,
        HASHTAG_PATTERN,
        COMMAND_RANDOM,
        NON_VALUE_PATTERN,
    ]
