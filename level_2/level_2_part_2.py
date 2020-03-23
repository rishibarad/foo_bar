from functools import *


def solution(xs):
    # Your code here
    neg_nums = []

    if not xs:
        return "0"
    elif len(xs) == 1:
        return str(xs[0])

    for num in xs:
        if num < 0:
            neg_nums.append(num)

    while 0 in xs:
        xs.remove(0)

    if len(neg_nums) == 1 and len(xs) == 1:
        return "0"

    if len(neg_nums) % 2 != 0:
        greatest_neg = max(neg_nums)
        xs.remove(greatest_neg)

    max_prod = reduce(lambda x, y: x * y, xs)
    return str(max_prod)


def main():
    test_0 = solution([2, -3, 1, 0, -5])
    print("test 0:\n", test_0)
    test_1 = solution([2, 0, 2, 2, 0])
    print("test 1:\n", test_1)
    test_2 = solution([-2, -3, 4, -5])
    print("test 2:\n", test_2)
    test_3 = solution([-7, -1, 4, 5])
    print("test 3:\n", test_3)
    test_4 = solution([0, 3])
    print("test 4:\n", test_4)
    test_5 = solution([-4, -1])
    print("test 5:\n", test_5)
    test_6 = solution([-1, -1])
    print("test 6:\n", test_6)
    test_7 = solution([-8])
    print("test 7:\n", test_7)
    test_8 = solution([-5, 3])
    print("test 8:\n", test_8)
    test_9 = solution([5])
    print("test 9:\n", test_9)
    test_10 = solution([0])
    print("test 10:\n", test_10)
    test_11 = solution([2, 2, 2, 0, 0, -1, 0, -7])
    print("test 11:\n", test_11)
    test_12 = solution([-2, 2, 2, 2, -1, -7])
    print("test 12:\n", test_12)
    test_13 = solution([-2, 2, 2, 2, -3, -7])
    print("test 13:\n", test_13)
    # potential test: 0 0 0 0 -7
    pass


if __name__ == "__main__":
    main()