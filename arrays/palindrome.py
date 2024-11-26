from collections import deque
from typing import Deque
from math import floor


class Solution:
    """
    Given an integer x, return true if x is a
    palindrome
    , and false otherwise.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

    Constraints:
    -231 <= x <= 231 - 1

    Follow up: Could you solve it without converting the integer to a string?

    123 => 123/ 10 => 12 + 3
                   => 12 + 3 * 10
                   => 12/ 10 + 30
                   => 1 + 2 * 10 + 30 * 10
                   => 321
    """

    def is_palindrome_str(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == x[::-1]

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            x *= -1

        remainder = x
        total = 0
        while remainder > 0:
            remainder, quotient = divmod(remainder, 10)
            total = total * 10 + quotient

        return x == total

    def is_palindrome_v2(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        remainder = 0
        total = 0
        while x > remainder:
            remainder = remainder * 10 + x % 10
            x //= 10
        # 123404321 For palindrome, exactly at halfish they become equal or greater, in this case greater
        # # 12344321 equal in this case. Safe to exit

        return x == total or x == remainder // 10


if __name__ == "__main__":
    assert True == Solution().isPalindrome(121)
    assert True == Solution().isPalindrome(0)
