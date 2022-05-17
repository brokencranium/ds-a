def str_to_zigzag(s, numRows: int) -> str:

    if numRows == 1:
        return s

    result = ""
    for i in range(numRows):
        for j in range(i, len(s), 2 * numRows - 2):
            result += s[j]
            if i != 0 and i != numRows - 1 and j + 2 * numRows - 2 - i < len(s):
                result += s[j + 2 * numRows - 2 - i]
    return result

    # for i in range(1, numRows + 1, 1):
    #     for j in range(i, len(s), 2 * numRows - 2):
    #         if i == 0 or i == numRows - 1:
    #             result += s[j]
    #         else:
    #             step = j + 2 * numRows - 2 - 2 * i
    #             if step < len(s):
    #                 result += s[j] + s[j + (2 * numRows - 2) - (2 * i)]
    #             else:
    #                 result += s[j]
    #
    # return result


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    print("Length", len(s))
    # print(str_to_zigzag(s, 3))
    # print(str_to_zigzag(s, 4))
    # print(str_to_zigzag(s, 5))
    print(str_to_zigzag("A", 1))
