"""level 3"""


def solution(x):
    curr_max, curr_min, max_prod = 1, 1, 1
    pos_check = False

    for num in x:
        if num > 0:
            curr_max *= num
            curr_min = min(curr_min * num, 1)
            pos_check = True
        elif num < 0:
            old_max = curr_max
            curr_max = max(curr_min * num, 1)
            curr_min = old_max * num
        if max_prod < curr_max:
            max_prod = curr_max

    if max_prod == 1 and not pos_check:
        return 0
    return max_prod


def main():
    test_1 = solution([2, 0, 2, 2, 0])
    print("test 1:\n", test_1)
    test_2 = solution([-2, -3, 4, -5])
    print("test 2:\n", test_2)
    test_3 = solution([-7, -1, 4, 5])
    print("test 2:\n", test_3)
    pass


if __name__ == "__main__":
    main()