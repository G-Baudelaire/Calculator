class GeneralMethods:
    UPPER_BOUND = 2147483647
    LOWER_BOUND = -2147483648

    @staticmethod
    def bound_output(integer: int) -> int:

        """
        Will make the result stay within the upper and lower bounds of the SRPN calculator.
        :param integer: Integer to be bounded.
        :return: The given integer within a valid range.
        """
        if integer > GeneralMethods.UPPER_BOUND:
            return GeneralMethods.UPPER_BOUND
        elif integer < GeneralMethods.LOWER_BOUND:
            return GeneralMethods.LOWER_BOUND
        else:
            return integer
