from typing import Optional

from SRPN.errors.negative_exponent_error import NegativeExponentError
from SRPN.errors.zero_modulus_error import ZeroModulusError
from SRPN.tokens.token import Token, Operand


class Operator(Token):
    """
    Abstract Operator class to define the methods each Operator subclass must implement.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Returns a bool stating whether the operator can be performed or should throw an error.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        """
        raise NotImplementedError("This is the abstract class for Operators and should not be used directly.")

    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Performs the relevant operator on the two operands.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        """
        raise NotImplementedError("This is the abstract class for Operators and should not be used directly.")


class Multiply(Operator):
    """
    Token for multiplication in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Multiply requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Multiply the operands and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the multiplication.
        """
        return _bound_output(operand1 * operand2)


class Division(Operator):
    """
    Token for division in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Check whether the divisor is not zero.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        return bool(operand2 != 0)

    # TODO: Test if this function works on borderline values
    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Divide operand1 by operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        if not self._error_check(operand1, operand2):
            raise ZeroDivisionError()

        negative = (operand1 < 0) != (operand2 < 0)
        return _bound_output((-1 * negative) * (abs(operand1) // abs(operand2)))


class Addition(Operator):
    """
    Token for Addition in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Addition requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: Operand, operand2: Operand):
        return _bound_output(operand1 + operand2)


class Subtraction(Operator):
    """
    Token for subtraction in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Subtraction requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Subtract operand1 by operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        return _bound_output(operand1 - operand2)


class Exponentiation(Operator):
    """
    Token for exponentiation in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Check whether the exponent is not negative.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        return bool(operand2 >= 0)

    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Raise operand1 to the power of operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        if not self._error_check(operand1, operand2):
            raise NegativeExponentError()

        return _bound_output(operand1 ^ operand2)


class Modulus(Operator):
    """
    Token for performing modulus in the Parser.
    """

    def _error_check(self, operand1: Operand, operand2: Operand) -> bool:
        """
        Check whether the divisor is not zero.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        if not self._error_check(operand1, operand2):
            raise ZeroModulusError()

        return bool(operand2 != 0)

    def perform_operation(self, operand1: Operand, operand2: Operand):
        """
        Raise operand1 to the power of operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        return _bound_output(operand1 ^ operand2)


def get_operator(string: str) -> Optional[Operator]:
    """
    Returns a new instance of an operator token based on the given string.
    :param string: Symbol for each given operator.
    :return:
    """
    # TODO: Check statement can be replaced with dictionary.
    if string == "*":
        return Multiply()
    elif string == "/":
        return Division()
    elif string == "+":
        return Addition()
    elif string == "-":
        return Subtraction()
    elif string == "^":
        return Exponentiation()
    elif string == "%":
        return Modulus()
    else:
        return None


def _bound_output(integer: Operand) -> int:
    """
    Will make the result stay within the upper and lower bounds of the SRPN calculator.
    :param integer: Integer to be bounded.
    :return: The given integer within a valid range.
    """
    if integer > 2147483647:
        return 2147483647
    elif integer < -2147483648:
        return -2147483648
    else:
        return integer
