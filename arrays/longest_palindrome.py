# find the longest palindrome in a string by comparing the center of the string
# with the center of the substring
# O(n^2) time complexity
# O(1) space complexity
# Need to consider even and odd length palindromes. For odd length palindromes, index of center is the same
# as the index of the center of the substring. For even length palindromes, the index of the center of the substring
# is the same as the index of the center of the substring minus 1 or plus 1.

class Solution:
    @staticmethod
    def get_palindrome_substring( input_str, left, right) -> str:
        while left >= 0 and right < len(input_str) and input_str[left] == input_str[right]:
            left -= 1
            right += 1

        return input_str[left + 1: right]

    def longest_palindrome(self, s: str) -> str:
        longest_pal = ""
        for index in range(len(s)):
            substr_pal = self.get_palindrome_substring(s, index, index)
            if len(longest_pal) < len(substr_pal):
                longest_pal = substr_pal

            substr_pal = self.get_palindrome_substring(s, index, index + 1)
            if len(longest_pal) < len(substr_pal):
                longest_pal = substr_pal

        return longest_pal


if __name__ == "__main__":
    s = Solution()
    print(s.longest_palindrome("babad"))
    print(s.longest_palindrome("babad"))
    print(s.longest_palindrome("babadada"))
    print(s.longest_palindrome("aba"))
    print(s.longest_palindrome("acbbcd"))
    print(s.longest_palindrome("acbbcd"))
    print(s.longest_palindrome("cbbd"))
