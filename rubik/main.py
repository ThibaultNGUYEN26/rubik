from utils.scramble_parsing import scramble_parsing
from utils.random_scramble import generate_random_moves
from utils.visualizer import start_rubiks_visualizer
import argparse
import random

# List of all valid moves in Rubik's cube
valid_move_list = ["F", "F'", "F2", "R", "R'", "R2", "U", "U'", "U2", "B", "B'", "B2", "L", "L'", "L2", "D", "D'", "D2"]

def main():
    # Different arguments to pass
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
    print(scramble)

    # Show visualizer if -v is specified
    if args.visualizer:
        start_rubiks_visualizer(moves)

if __name__ == "__main__":
    main()
