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
    'U': [['W', 'W', 'W'],
          ['W', 'W', 'W'],
          ['W', 'W', 'W']],
    'F': [['G', 'G', 'G'],
          ['G', 'G', 'G'],
          ['G', 'G', 'G']],
    'R': [['R', 'R', 'R'],
          ['R', 'R', 'R'],
          ['R', 'R', 'R']],
    'B': [['B', 'B', 'B'],
          ['B', 'B', 'B'],
          ['B', 'B', 'B']],
    'L': [['O', 'O', 'O'],
          ['O', 'O', 'O'],
          ['O', 'O', 'O']],
    'D': [['Y', 'Y', 'Y'],
          ['Y', 'Y', 'Y'],
          ['Y', 'Y', 'Y']]
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
    print("Cube state after moves:")
    for face, grid in cube.items():
        print(f"{face} face:")
        for row in grid:
            print(" ".join(row))
        print()

    # Show visualizer if -v is specified
    if args.visualizer:
        start_rubiks_visualizer(moves)

if __name__ == "__main__":
    main()
