"""level 1"""


def solution(x):
    squares = []
    i = 1
    while x > 0:
        if i ** 2 > x:
            sqr = (i - 1) ** 2
            x -= sqr
            i = 1
            squares.append(sqr)
        else:
            i += 1

    return squares


def main():
    test_1 = solution(15324)
    print("test 1:\n", test_1)
    test_2 = solution(12)
    print("test 2:\n", test_2)
    pass


if __name__ == "__main__":
    main()
