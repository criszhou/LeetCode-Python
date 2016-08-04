class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        retList = [];

        while num >= 1000:
            retList.append('M');
            num -= 1000
        if num >= 900:
            retList.append('CM');
            num -= 900
        if num >= 500:
            retList.append('D');
            num -= 500
        if num >= 400:
            retList.append('CD');
            num -= 400

        retList.append('C' * (num // 100))
        num %= 100

        if num >= 90:
            retList.append('XC');
            num -= 90
        if num >= 50:
            retList.append('L');
            num -= 50
        if num >= 40:
            retList.append('XL');
            num -= 40
        retList.append('X' * (num // 10))
        num %= 10

        if num >= 9:
            retList.append('IX');
            num -= 9
        if num >= 5:
            retList.append('V');
            num -= 5
        if num >= 4:
            retList.append('IV');
            num -= 4
        retList.append('I' * num)

        return "".join(retList);