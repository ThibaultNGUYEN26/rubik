# Parse if the scramble is valid and return the list of the scramble
def scramble_parsing(scramble, valid_move_list):
    scramble = scramble.upper().strip()
    moves = scramble.split()
    for move in moves:
        if move not in valid_move_list:
            return False, f"Wrong move! -> {move}"
    return True, moves
