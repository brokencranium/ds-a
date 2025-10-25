class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        if x < 10:
            return True

        remainder = 0
        while x > remainder:
            remainder = remainder * 10 + x % 10
            x = x // 10

        return x == remainder or x == remainder // 10


if __name__ == "__main__":
    result = Solution().isPalindrome(121)
    assert result == True, f"Expected True but got {result}"

    result = Solution().isPalindrome(-121)
    assert result == False, f"Expected False but got {result}"
