from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        for index, element in enumerate(s):
            if counter.get(element) == 1:
                return index

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.firstUniqChar("loveleetcode"))