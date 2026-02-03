table_score = {}


def print_board(board):
    print("\n")
    display = [str(i+1) if board[i] == ' ' else board[i] for i in range(9)]
    print(f" {display[0]} | {display[1]} | {display[2]} ")
    print("-----------")
    print(f" {display[3]} | {display[4]} | {display[5]} ")
    print("-----------")
    print(f" {display[6]} | {display[7]} | {display[8]} ")
    print("\n")


def get_player_move():
    move = input(f"Player X, enter position (1-9): ")
    return int(move) - 1


def get_computer_move(table, depth):
    min_move = None
    min_score = 1

    if not ''.join(table) in table_score:
        calc_table(table, depth)

    for i in range(9):
        if min_score == -1:
            return min_move
        if table[i] == ' ':
            if min_move != None:
                potential_move = table[:]
                potential_move[i] = 'O'
                if min_score > table_score[''.join(potential_move)]:
                    min_move = i
                    min_score = table_score[''.join(potential_move)]
            else:
                min_move = i
                potential_move = table[:]
                potential_move[i] = 'O'
                min_score = table_score[''.join(potential_move)]

    return min_move
                
def calc_table(table, depth):
    table_result = eval_table(table)

    if table_result != '-':
        table_score[''.join(table)] = {
            'X': 1,
            ' ': 0,
            'O': -1
        }[eval_table(table)]
    else:
        minmax = 1 if depth % 2 == 0 else -1

        for i in range(9):
            if table[i] == ' ':
                potential_move = table[:]
                potential_move[i] = 'X' if (depth + 1) % 2 == 0 else 'O'
                calc_table(potential_move, depth + 1)
                if depth % 2 == 0 and table_score[''.join(potential_move)] < minmax:
                    minmax = table_score[''.join(potential_move)]
                elif depth % 2 == 1 and table_score[''.join(potential_move)] > minmax:
                    minmax = table_score[''.join(potential_move)]
        
        table_score[''.join(table)] = minmax

# ['X', 'X', 'X', ...]
def eval_table(table):
    # rows
    for i in range(3):
        if table[0 + 3 * i] == table[1 + 3 * i] == table[2 + 3 * i] != ' ':
            return table[0 + 3 * i]

    # columns
    for i in range(3):
        if table[0 + i] == table[3 + i] == table[6 + i] != ' ':
            return table[0 + i]

    # diagonals 0, 4, 8 and 2, 4, 6
    for i in range(2):
        if table[4] == table[i * 2] == table[8 - 2 * i] != ' ':
            return table[4]

    return ' ' if not ' ' in table else '-'

def main():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, computer is O")
    print("Available positions will be shown as numbers\n")

    depth = 0

    # Game loop
    while True:
        print_board(board)


        if eval_table(board) == '-':
            if current_player == 'X':
                position = get_player_move()
            else:
                position = get_computer_move(board, depth)
                print(f"Player O chose position {position + 1}")

            board[position] = current_player
            if not ''.join(board) in table_score:
                calc_table(board, depth)

            current_player = 'O' if current_player == 'X' else 'X'
            depth += 1
        else:
            result = eval_table(board)
            if result == ' ':
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break


if __name__ == "__main__":
    main()
