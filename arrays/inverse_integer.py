class Solution:
    @staticmethod
    def is_32_bit(n) -> bool:
        # works for both positive and negative
        # can also use range -2 ** 31 <= n <= 2 ** 31 - 1
        return n < 1 << 31

    def reverse(self, x: int) -> int:
        if not self.is_32_bit(x):
            return 0

        inverse = 1
        if x < 0:
            inverse = -1

        abs_x = x * inverse
        value = str(abs_x)
        value = value[::-1]

        try:
            value = int(value)

            if not self.is_32_bit(value):
                return 0
        except:
            return 0

        return value * inverse


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))
    print(solution.reverse(-2147483648))
    print(solution.reverse(0))
    print(solution.reverse(1))
    print(solution.reverse(-1))
    print(solution.reverse(123))
