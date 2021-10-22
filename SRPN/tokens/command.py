from typing import Optional

from SRPN.tokens.token import Token


class Command(Token):
    pass


class OutputStack(Command):
    pass

class OutputTopOfStack(Command):
    pass