import numpy as np
from moves import *
import sys

# Define the colors for each face of the Rubik's Cube
colors = {
    0: 'white',
    1: 'orange',
    2: 'green',
    3: 'red',
    4: 'blue',
    5: 'yellow'
}

"""
	  W W W
      W W W
      W W W
O O O G G G R R R B B B
O O O G G G R R R B B B
O O O G G G R R R B B B
      Y Y Y
      Y Y Y
      Y Y Y 

TOP   LEFT  FRONT ORANGE BACK BOTTOM
W W W O O O G G G R R R B B B Y Y Y
W W W O O O G G G R R R B B B Y Y Y
W W W O O O G G G R R R B B B Y Y Y

0  1  2  W W W 0
3  4  5  W W W 0
6  7  8  W W W 0

9  10 11 O O O 1
12 13 14 O O O 1
15 16 17 O O O 1

18 19 20 G G G 2
21 22 23 G G G 2
24 25 26 G G G 2

27 28 29 R R R 3
30 31 32 R R R 3
33 34 35 R R R 3

36 37 38 B B B 4
39 40 41 B B B 4
42 43 44 B B B 4

45 46 47 Y Y Y 5
48 49 50 Y Y Y 5
51 52 53 Y Y Y 5
"""

cube = np.array([[0, 0, 0], [0, 0, 1], [0, 0, 2],
                 [0, 1, 0], [0, 1, 1], [0, 1, 2],
                 [0, 2, 0], [0, 2, 1], [0, 2, 2], 

				 [1, 0, 0], [1, 0, 1], [1, 0, 2],
                 [1, 1, 0], [1, 1, 1], [1, 1, 2],
                 [1, 2, 0], [1, 2, 1], [1, 2, 2], 

                 [2, 0, 0], [2, 0, 1], [2, 0, 2],
                 [2, 1, 0], [2, 1, 2], [2, 1, 2],
                 [2, 2, 0], [2, 2, 1], [2, 2, 2], 

                 [3, 0, 0], [3, 0, 1], [3, 0, 2],
                 [3, 1, 0], [3, 1, 1], [3, 1, 2],
                 [3, 2, 0], [3, 2, 1], [3, 2, 2], 

                 [4, 0, 0], [4, 0, 1], [4, 0, 2],
                 [4, 1, 0], [4, 1, 1], [4, 1, 2],
                 [4, 2, 0], [4, 2, 1], [4, 2, 2], 

                 [5, 0, 0], [5, 0, 1], [5, 0, 2],
                 [5, 1, 0], [5, 1, 1], [5, 1, 2],
                 [5, 2, 0], [5, 2, 1], [5, 2, 2]])

shuffle = " ".join(sys.argv[1:])
shuffle_list = shuffle.split()
shuffle_list = [c.upper() for c in shuffle_list]

moves = {
    "U": u_move,
    "U'": u_prime_move,
    "U2": lambda cube: u_move(u_move(cube)),
    "L": l_move,
    "L'": l_prime_move,
    "L2": lambda cube: l_move(l_move(cube)),
    "F": f_move,
    "F'": f_prime_move,
    "F2": lambda cube: f_move(f_move(cube)),
    "R": r_move,
    "R'": r_prime_move,
    "R2": lambda cube: r_move(r_move(cube)),
    "B": b_move,
    "B'": b_prime_move,
    "B2": lambda cube: b_move(b_move(cube)),
    "D": d_move,
    "D'": d_prime_move,
    "D2": lambda cube: d_move(d_move(cube))
}

for move in shuffle_list:
    if move not in moves:
        print("Error: Invalid move -", move)
        exit()
    cube = moves[move](cube)

first_word = True
count = 0
color_codes = ["\033[37m", "\033[38;5;202m", "\033[32m", "\033[91m", "\033[34m", "\033[93m"]
reset_code = "\033[0m"

for i, row in enumerate(cube):
    face_index, _, _ = row
    color = colors[face_index]

    if first_word and count < 6:
        print(f"\n{color_codes[count]}{colors[count].upper()}{reset_code} :")
        print("_" * 28)

        count += 1
        first_word = False

    if color == "white":
        print(f"|{color_codes[0]} {format(color, '<6')}{reset_code} ", end="")
    elif color == "orange":
        print(f"|{color_codes[1]} {format(color, '<6')}{reset_code} ", end="")
    elif color == "green":
        print(f"|{color_codes[2]} {format(color, '<6')}{reset_code} ", end="")
    elif color == "red":
        print(f"|{color_codes[3]} {format(color, '<6')}{reset_code} ", end="")
    elif color == "blue":
        print(f"|{color_codes[4]} {format(color, '<6')}{reset_code} ", end="")
    elif color == "yellow":
        print(f"|{color_codes[5]} {format(color, '<6')}{reset_code} ", end="")

    if (i + 1) % 3 == 0:
        if i % 3 == 2:
            print(f"{reset_code}|")
            print("_" * 28)

        if (i + 1) % 9 == 0:
            first_word = True
