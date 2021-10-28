from SRPN.errors.negative_exponent_error import NegativeExponentError
from SRPN.tokens import general_methods, token


class Operator(token.Token):
    """
    Abstract Operator class to define the methods each Operator subclass must implement.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Returns a bool stating whether the operator can be performed or should throw an error.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        """
        raise NotImplementedError("This is the abstract class for Operators and should not be used directly.")

    def perform_operation(self, operand1: int, operand2: int):
        """
        Performs the relevant operator on the two operands.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        """
        raise NotImplementedError("This is the abstract class for Operators and should not be used directly.")


class Product(Operator):
    """
    Token for multiplication in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Multiply requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: int, operand2: int):
        """
        Multiply the operands and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the multiplication.
        """
        return general_methods.GeneralMethods.bound_output(operand1 * operand2)


class Quotient(Operator):
    """
    Token for division in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Check whether the divisor is not zero.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        return bool(operand2 != 0)

    # TODO: Test if this function works on borderline values
    def perform_operation(self, operand1: int, operand2: int):
        """
        Divide operand1 by operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        if not self._error_check(operand1, operand2):
            raise ZeroDivisionError("Divide by 0.")

        is_output_negative = (operand1 < 0) != (operand2 < 0)
        absolute_value_of_quotient = abs(operand1) // abs(operand2)
        quotient = absolute_value_of_quotient if not is_output_negative else -1 * absolute_value_of_quotient
        return general_methods.GeneralMethods.bound_output(quotient)


class Addition(Operator):
    """
    Token for Addition in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Addition requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: int, operand2: int):
        return general_methods.GeneralMethods.bound_output(operand1 + operand2)


class Subtraction(Operator):
    """
    Token for subtraction in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Subtraction requires no checks.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: True
        """
        return True

    def perform_operation(self, operand1: int, operand2: int):
        """
        Subtract operand1 by operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        return general_methods.GeneralMethods.bound_output(operand1 - operand2)


class Exponentiation(Operator):
    """
    Token for exponentiation in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Check whether the exponent is not negative.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        return bool(operand2 >= 0)

    def perform_operation(self, operand1: int, operand2: int):
        """
        Raise operand1 to the power of operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        if not self._error_check(operand1, operand2):
            raise NegativeExponentError("Negative power.")

        return general_methods.GeneralMethods.bound_output(operand1 ** operand2)


class Modulo(Operator):
    """
    Token for performing modulus in the Parser.
    """

    def _error_check(self, operand1: int, operand2: int) -> bool:
        """
        Check whether the divisor is not zero.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: Boolean.
        """
        return bool(operand2 != 0)

    def perform_operation(self, operand1: int, operand2: int):
        """
        Raise operand1 to the power of operand2 and round the output to the calculator bounds.
        :param operand1: The operand to the left of the operator.
        :param operand2: The operand to the right of the operator.
        :return: A bounded output of the division.
        """
        if not self._error_check(operand1, operand2):
            raise ZeroDivisionError("Divide by 0.")

        return general_methods.GeneralMethods.bound_output(operand1 % operand2)
