class Solution(object):
    def myAtoi(self, num):
        """
        :type num: str
        :rtype: int
        """
        import re

        re_spaces = r"\s*"
        re_sign = r"(?P<sign>[+-]?)"
        re_digits = r"(?P<digits>\d*)"

        match = re.match(re_spaces + re_sign + re_digits + re_spaces, num)

        str_sign = match.group("sign")
        sign = -1 if str_sign == "-" else +1

        str_digits = match.group("digits")
        digits = int(str_digits) if str_digits else 0

        ret = sign * digits

        ret = min(ret, +2147483647)
        ret = max(ret, -2147483648)

        return ret