from typing import Optional


class Command:
    pass


class DisplayStack(Command):
    pass


def get_command(string: str) -> Optional[DisplayStack]:
    if string == "d":
        return DisplayStack()
    else:
        return None
