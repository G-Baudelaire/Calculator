from SRPN.tokens.token import Token


class Operand(Token):
    def __init__(self, string: str):
        if string.isdecimal():

