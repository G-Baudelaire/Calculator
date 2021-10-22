from SRPN.errors.underflow_error import UnderflowError
from SRPN.tokens.operators import Operator


class Stack:
    def __len__(self):
        return len(self._memory)

    def __init__(self):
        self._memory = [-2147483648]
        self._new_stack = True

    def add_to_stack(self, value: int) -> bool:
        if self._new_stack:
            self._memory = [value]
            self._new_stack = False
        elif len(self._memory) == 23:
            raise OverflowError("Stack cannot hold more than 23 operands")
        else:
            self._memory.append(value)

    def perform_operand(self, operator: Operator):
        if len(self._memory) == 1:
            raise UnderflowError("Stack only has one operand")
        else:
            output = operator.perform_operation(self._memory[-2], self._memory[-1])
            self._memory[-1] = output
