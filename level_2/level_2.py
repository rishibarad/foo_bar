"""level 2"""



def solution(src, dest):
    # convert to rows and columns
    s_row, d_row = int(src / 8), int(dest / 8)
    s_col, d_col = src % 8, dest % 8

    # movement possibilities for the knight
    knight_moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

    # initialize board with -1. represents unvisited positions
    chess_board =

    # queue for storing knight moves with distances. initialized with starting position
    move_queue = [[s_row, s_col, 0]]


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
