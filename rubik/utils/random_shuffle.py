import random

# Generate a random sequence of Rubik's cube moves, avoiding contradictory consecutive moves.
def generate_random_moves(n, valid_move_list):
    moves = []
    previous_move = None

    for _ in range(n):
        while True:
            move = random.choice(valid_move_list)
            # Avoid contradictory moves like F followed by F' or F2
            if previous_move and move[0] == previous_move[0]:  # Same face
                continue
            moves.append(move)
            previous_move = move
            break

    return " ".join(moves)
