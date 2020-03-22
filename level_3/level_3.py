"""level 3"""


def solution(xs):
    pos_prod, neg_prod = 1, 1
    greatest_neg = None
    non_zero = 0

    for num in xs:
        if num > 0:
            pos_prod *= num
            non_zero += 1
        elif num < 0:
            if greatest_neg is None or num > greatest_neg:
                greatest_neg = num
            neg_prod *= num
            non_zero += 1

    if non_zero == 0:
        return str(0)
    elif non_zero == 1:
        if neg_prod < 0:
            return str(neg_prod)
        else:
            return str(pos_prod)
    elif neg_prod < 0 and greatest_neg is not None:
        neg_prod = int(neg_prod / greatest_neg)
        return str(pos_prod * neg_prod)
    elif neg_prod > 0:
        return str(pos_prod * neg_prod)
    else:
        return str(pos_prod)



def main():
    test_0 = solution([2, -3, 1, 0, -5])
    print("test 0:\n", test_0)
    test_1 = solution([2, 0, 2, 2, 0])
    print("test 1:\n", test_1)
    test_2 = solution([-2, -3, 4, -5])
    print("test 2:\n", test_2)
    test_3 = solution([-7, -1, 4, 5])
    print("test 3:\n", test_3)
    test_4 = solution([0, 5])
    print("test 4:\n", test_4)
    test_5 = solution([-5, -1])
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
    pass


if __name__ == "__main__":
    main()