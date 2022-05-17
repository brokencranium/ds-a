# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).
#
# The function first discards as many whitespace characters as necessary until the first
# non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed
# by as many numerical digits as possible,
# and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the
# 32-bit signed integer range: [−231,  231 − 1].
# If the numerical value is out of the range of representable values,
# INT_MAX (231 − 1) or INT_MIN (−231) is returned.


class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if not s:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else:
            sign = 1
        res = 0
        for i in range(len(s)):
            if s[i] not in '0123456789':
                break
            res = res * 10 + int(s[i])
        res = sign * res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if res < -2 ** 31:
            return -2 ** 31
        return res

    def myAtoi_v1(self, input: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(input)

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        # Discard all spaces from the beginning of the input string.
        while index < n and input[index] == ' ':
            index += 1

        # sign = +1, if it's positive number, otherwise sign = -1.
        if index < n and input[index] == '+':
            sign = 1
            index += 1
        elif index < n and input[index] == '-':
            sign = -1
            index += 1

        # Traverse next digits of input and stop if it is not a digit.
        # End of string is also non-digit character.
        while index < n and input[index].isdigit():
            digit = int(input[index])

            # Check overflow and underflow conditions.
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.
                return INT_MAX if sign == 1 else INT_MIN

            # Append current digit to the result.
            result = 10 * result + digit
            index += 1

        # We have formed a valid number without any overflow/underflow.
        # Return it after multiplying it with its sign.
        return sign * result

    def my_atoi(self, s: str) -> int:
        power = 0
        result = 0
        sign = 1
        for val in reversed(s):
            if val == '-':
                sign = -1

            if val in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                result = result + int(val) * 10 ** power
                power += 1

        result *= sign

        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.my_atoi("42"))
