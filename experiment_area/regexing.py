import re

# non_value must be the final expression matched, order is irrelevant for every other match.
from typing import List

space_character = r" "
plus = r"\+"
minus = r"-"
multiply = r"\*"
divide = r"\/"
modulus = r"%"
exponent = r"\^"
digits = r"\d+"
letter_d = r"d"
equals = r"="
hashtag = r"#"
non_value = r"."
patterns = [
    space_character, plus, minus, multiply, divide, modulus, exponent, digits, letter_d, equals, hashtag, non_value
]

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
STRING_TYPES = [
    SPACE_CHARACTER, PLUS, MINUS, MULTIPLY, DIVIDE, MODULUS, EXPONENT, DIGITS, LETTER_D, EQUALS, HASHTAG, NON_VALUE
]