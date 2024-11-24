from utils.shuffle_parsing import shuffle_parsing
from utils.visualizer import start_rubiks_visualizer
import argparse

def main():
    parser = argparse.ArgumentParser(description="Process Rubik's cube moves.")
    parser.add_argument("moves", type=str, help="Rubik's cube moves as a string (e.g., 'F R U2 B' L' D')")
    parser.add_argument("-v", "--visualizer", action="store_true", help="Launch the Rubik's cube visualizer")

    args = parser.parse_args()
    moves = args.moves

    shuffle = shuffle_parsing(moves)
    print(shuffle)

    if args.visualizer:
        start_rubiks_visualizer()

if __name__ == "__main__":
    main()
