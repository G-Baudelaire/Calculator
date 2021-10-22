from typing import Tuple

from SRPN.errors.negative_exponent_error import NegativeExponentError
from SRPN.errors.stack_empty_error import StackEmptyError
from SRPN.errors.underflow_error import UnderflowError
from SRPN.errors.zero_modulus_error import ZeroModulusError
from SRPN.stack.stack import Stack
from SRPN.tokens import operand, token, operators, command


class Parser:
    def read_tokens(self, stack: Stack, tokens: Tuple[token.Token, ...]):
        for _token in tokens:
            token_class = type(_token)
            if issubclass(token_class, operand.Operand):
                self._read_operand_token(_token, stack)
            elif issubclass(token_class, operators.Operator):
                self._read_operator_token(_token, stack)
            elif issubclass(token_class, command.Command):
                self._read_command_token(_token, stack)

    def _read_operand_token(self, _operand: operand.Operand, stack: Stack):
        try:
            stack.add_int_to_stack(_operand.get_value())
        except OverflowError as e:
            print(e)

    def _read_operator_token(self, _operator: operators.Operator, stack: Stack):
        try:
            stack.perform_operand(_operator)
        except (UnderflowError, ZeroDivisionError, NegativeExponentError,) as e:
            print(e)
        except ZeroModulusError as e:
            print(e)
            exit(136)

    def _read_command_token(self, _command: command.Command, stack: Stack):
        try:
            _command.perform_command(stack)
        except (StackEmptyError, OverflowError) as e:
            print(e)
