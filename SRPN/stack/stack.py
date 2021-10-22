from random import randint, seed

from SRPN.errors.stack_empty_error import StackEmptyError
from SRPN.errors.underflow_error import UnderflowError
from SRPN.tokens.general_methods import GeneralMethods
from SRPN.tokens.operators import Operator


class Stack:
    # I know this isn't really a stack but it's to fit with the output used in SRPN.
    def __len__(self):
        return len(self._memory)

    def __init__(self):
        seed(a=0, version=2)
        self._memory = [-2147483648]
        self._new_stack = True

    def is_new_stack(self):
        return self._new_stack

    def get_stack_memory(self):
        return tuple(self._memory)

    def get_equals(self):
        if self._new_stack:
            raise StackEmptyError("Stack Empty")
        else:
            return self._memory[-1]

    def add_int_to_stack(self, value: int) -> bool:
        if self._new_stack:
            self._memory = [value]
            self._new_stack = False
        elif len(self._memory) == 23:
            raise OverflowError("Stack overflow.")
        else:
            self._memory.append(value)

    def add_random_int_to_stack(self):
        self.add_int_to_stack(randint(0, GeneralMethods.UPPER_BOUND))

    def perform_operand(self, operator: Operator):
        if len(self._memory) == 1:
            raise UnderflowError("Stack underflow.")
        else:
            output = operator.perform_operation(self._memory[-2], self._memory[-1])
            self._memory[-2] = output
            self._memory = self._memory[:-1]
