class GeneralMethods:
    @staticmethod
    def bound_output(integer: int) -> int:
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
