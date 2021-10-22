from SRPN.stack.stack import Stack
from SRPN.tokens.token import Token


class Command(Token):
    def perform_command(self, stack: Stack):
        NotImplementedError("Abstract class.")


class OutputStack(Command):
    def perform_command(self, stack: Stack):
        for i in stack.get_stack_memory():
            print(i)


class OutputTopOfStack(Command):
    def perform_command(self, stack: Stack):
        string = stack.get_equals()
        print(string)


class StoreRandomInteger(Command):
    def perform_command(self, stack: Stack):
        string = stack.add_random_int_to_stack()
        print(string)
