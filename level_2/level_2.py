"""level 2"""


def solution(src, dest):
    start_pos = [int(src / 8), src % 8]
    end_pos = [int(dest / 8), dest % 8]
    # movement possibilities for the knight
    knight_moves = [[1, 2], [1, -2], [2, 1], [2, -1], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
    # initialize chess board with -1 to represent unvisited positions
    chess_board = [[-1 for i in range(8)] for j in range(8)]
    # initialize starting position
    chess_board[start_pos[0]][start_pos[1]] = 0
    # queue storing knight moves
    move_queue = [start_pos]
    while len(move_queue) > 0:
        curr_pos = move_queue.pop(0)
        if curr_pos == end_pos:
            return chess_board[curr_pos[0]][curr_pos[1]]
        else:
            for m in knight_moves:
                new_pos = [curr_pos[0] + m[0], curr_pos[1] + m[1]]
                # check if position is valid
                if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 8:
                    # check if position is visited
                    if chess_board[new_pos[0]][new_pos[1]] == -1:
                        chess_board[new_pos[0]][new_pos[1]] = chess_board[curr_pos[0]][curr_pos[1]] + 1
                        move_queue.append(new_pos)


def main():
    test_1 = solution(0, 1)
    print("test 1:\n", test_1)
    test_2 = solution(19, 36)
    print("test 2:\n", test_2)
    pass


if __name__ == "__main__":
    main()
