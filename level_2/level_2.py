"""level 2"""


def solution(src, dest):
    s_row, d_row = int(src / 8), int(dest / 8)
    s_col, d_col = src % 8, dest % 8
    print(s_row, s_col)
    print(d_row, d_col)

    num_moves = 0
    return num_moves


def main():
    test_1 = solution(0, 1)
    print("test 1:\n", test_1)
    test_2 = solution(19, 36)
    print("test 2:\n", test_2)
    pass


if __name__ == "__main__":
    main()
