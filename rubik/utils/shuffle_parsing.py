# Parse if the shuffle is valid and return the list of the shuffle
def shuffle_parsing(shuffle, valid_move_list):
    shuffle = shuffle.upper().strip()
    moves = shuffle.split()
    for move in moves:
        if move not in valid_move_list:
            return f"Wrong move! -> {move}"
    return moves