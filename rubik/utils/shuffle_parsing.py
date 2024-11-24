valid_move_list = ["F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2", "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"]

def shuffle_parsing(shuffle):
    shuffle = shuffle.upper().strip()
    moves = shuffle.split()
    for move in moves:
        if move not in valid_move_list:
            return f"Wrong move! -> {move}"
    return moves