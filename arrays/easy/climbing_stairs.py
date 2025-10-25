def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    assert 3, climb_stairs(3)
    assert 5, climb_stairs(4)
