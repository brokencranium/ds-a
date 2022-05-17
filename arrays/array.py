# Juggling algorithm
# Move elements of size and of length n in an array

def gcd(lower: int, higher: int):
    if lower == 0:
        return higher

    return gcd(higher % lower, lower)


def juggle(elements: list, size=3):
    window = gcd(size, len(elements))
    for index in range(0, len(elements) - window, window):
        for i in range(size):
            print("elements[index + i]", elements[index:index+3])
            # temp = elements[index + i]
            # # print("temp", temp)
            # elements[index + i] = elements[index + i + size]
            # # print("elements[index + i]", elements[index + i])
            # elements[index + i + size] = temp
            # # print("elements[index + i + step_size]", elements[index + i + step_size])
            pass
        # print(elements)


def juggle_v1(elements: list, size=3):
    print(elements[size - 1:])
    print(elements[:size - 1])
    print(elements[size - 1:] + elements[:size - 1])

    return elements[size - 1:].extend(elements[:size + 1])


if __name__ == '__main__':
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(gcd(3, len(elements)))
    # print(juggle_v1(elements, 4))
    print(juggle(elements, 4))
