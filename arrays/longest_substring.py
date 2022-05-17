# Sliding window
# Longest Substring Without Repeating Characters
from collections import deque


class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        start_index = 0
        max_length = 0
        for index in range(len(s)):
            right_index = s[:index].rfind(s[index]) + 1
            if right_index > start_index:
                start_index = right_index

            max_length = max(max_length, index - start_index + 1)

        return max_length

    def longest_substring(self, s: str) -> int:
        max_length = 0
        temp = deque([])

        for index, val in enumerate(s):
            if val not in temp:
                temp.append(val)
                if len(temp) > max_length:
                    max_length = len(temp)
            else:
                if len(temp) > max_length:
                    max_length = len(temp)

                left_pointer = temp.index(val)
                [temp.popleft() for i in range(left_pointer+1)]
                temp.append(val)

        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index != None and index >= left and index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res


if __name__ == "__main__":
    s = Solution()
    # print(s.longest_substring("jbpnbwwd"), s.length_of_longest_substring("jbpnbwwd"))
    # print(s.longest_substring("abcabcbb"),s.length_of_longest_substring("abcabcbb"))
    # print(s.longest_substring("bbbbb"),s.length_of_longest_substring("bbbbb"))
    # print(s.longest_substring("pwwkew"),s.length_of_longest_substring("pwwkew"))
    # print(s.longest_substring("aab"),s.length_of_longest_substring("aab"))
    # print(s.longest_substring("dvdf"),s.length_of_longest_substring("dvdf"))
    # print(s.longest_substring("aabaab!bb"),s.length_of_longest_substring("aabaab!bb"))
    print(s.lengthOfLongestSubstring("aabaab!bb"))
