from utils.scramble_parsing import scramble_parsing
from utils.random_scramble import generate_random_moves
from utils.visualizer import start_rubiks_visualizer
from solver.movements import Uturn, Uprime, U2, Dturn, Dprime, D2, Fturn, Fprime, F2, Lturn, Lprime, L2, Rturn, Rprime, R2, Bturn, Bprime, B2
import argparse
import random

# List of all valid moves in Rubik's cube
valid_move_list = ["F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2", "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"]

# Cube definition
cube = {
    'U': [['W1', 'W2', 'W3'],
          ['W4', 'W5', 'W6'],
          ['W7', 'W8', 'W9']],
    'F': [['G1', 'G2', 'G3'],
          ['G4', 'G5', 'G6'],
          ['G7', 'G8', 'G9']],
    'R': [['R1', 'R2', 'R3'],
          ['R4', 'R5', 'R6'],
          ['R7', 'R8', 'R9']],
    'B': [['B1', 'B2', 'B3'],
          ['B4', 'B5', 'B6'],
          ['B7', 'B8', 'B9']],
    'L': [['O1', 'O2', 'O3'],
          ['O4', 'O5', 'O6'],
          ['O7', 'O8', 'O9']],
    'D': [['Y1', 'Y2', 'Y3'],
          ['Y4', 'Y5', 'Y6'],
          ['Y7', 'Y8', 'Y9']]
}

# Map of move strings to functions
move_functions = {
    "U": Uturn,
    "U'": Uprime,
    "U2": U2,
    "F": Fturn,
    "F'": Fprime,
    "F2": F2,
    "R": Rturn,
    "R'": Rprime,
    "R2": R2,
    "B": Bturn,
    "B'": Bprime,
    "B2": B2,
    "L": Lturn,
    "L'": Lprime,
    "L2": L2,
    "D": Dturn,
    "D'": Dprime,
    "D2": D2
}

def apply_moves(cube, moves):
    for move in moves:
        if move in move_functions:
            move_functions[move](cube)
        else:
            print(f"Invalid move: {move}")


# Define ANSI color codes
COLOR_CODES = {
    'W': '\033[1;97m',  # Bright White
    'G': '\033[1;92m',  # Bright Green
    'R': '\033[1;91m',  # Bright Red
    'B': '\033[1;94m',  # Bright Blue
    'O': '\033[1;33m',  # Bright Yellow-Orange (Orange approximation)
    'Y': '\033[1;93m',  # Bright Yellow
    'reset': '\033[0m'  # Reset to default
}

def colorize_facelet(facelet):
    # Extract the color code from the first character (e.g., 'W1', 'G2')
    color_char = facelet[0]
    color_code = COLOR_CODES.get(color_char, COLOR_CODES['reset'])
    return f"{color_code}{facelet}{COLOR_CODES['reset']}"

def display_colored_cube(cube):
    for face, grid in cube.items():
        print(f"{face} face:")
        for row in grid:
            # Apply color to each facelet
            colored_row = [colorize_facelet(facelet) for facelet in row]
            print(" ".join(colored_row))
        print()


def main():
    parser = argparse.ArgumentParser(description="Process Rubik's cube moves.")
    parser.add_argument("moves", nargs="?", type=str, help="Rubik's cube moves as a string (e.g., \"F R U2 B' L' D\")")
    parser.add_argument("-r", "--random", action="store_true", help="Generate a random sequence of moves")
    parser.add_argument("-v", "--visualizer", action="store_true", help="Launch the Rubik's cube visualizer")

    args = parser.parse_args()

    if args.random:
        # Generate random moves if -r is specified
        moves = generate_random_moves(20, valid_move_list)
        print(f"Random scramble generated: {moves}")
    elif args.moves:
        # Use provided moves
        moves = args.moves
    else:
        # If no moves are provided and -r is not specified, raise an error
        parser.error("You must specify moves or use --random to generate them.")

    # Parse if the scramble is valid, if so return a list of the scramble
    scramble = scramble_parsing(moves, valid_move_list)
    print(f"Scramble parsed: {scramble}")

    # Apply the moves to the cube
    apply_moves(cube, scramble)

    # Show the cube's state after applying the moves
    print("Cube state after moves:\n")
    display_colored_cube(cube)

    # Show visualizer if -v is specified
    if args.visualizer:
        start_rubiks_visualizer(moves)

if __name__ == "__main__":
    main()
