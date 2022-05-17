# Symbol       Value
# I             1 II III IV
# V             5  VI VII VIII IX
# X             10
# L             50
# C             100
# D             500
# M             1000
# 1, 10, 100, 1000 - Can be repeated 3 times in a row
# All Multiples of 5 - 1, 10, 100, 1000 can be represented leading I, X, C, M
#  530 500 + 30

class Solution:
    roman_digits = [
        ("I", "V", "X"),
        ("X", "L", "C"),
        ("C", "D", "M"),
        ("M", "", "")
    ]

    def intToRoman(self, num: int) -> str:
        result = ""

        for ones, fives, tens in self.roman_digits:
            num, int_digit = divmod(num, 10)
            if int_digit > 0:
                if int_digit <= 3:
                    rom_digits = [ones] * int_digit
                elif int_digit == 4:
                    rom_digits = [ones] + [fives]
                elif int_digit < 9:
                    rom_digits = [fives] + [ones] * (int_digit - 5)
                elif int_digit == 9:
                    rom_digits = [ones] + [tens]
                result = "".join(rom_digits) + result

        return result


if __name__ == '__main__':
    sol = Solution()
    result = sol.intToRoman(58)
    assert "LVIII" == result
