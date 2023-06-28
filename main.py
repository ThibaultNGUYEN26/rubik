import numpy as np
import tkinter as tk

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
41 42 43 B B B 4

44 45 46 Y Y Y 5
47 48 49 Y Y Y 5
50 51 52 Y Y Y 5
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

def u_move(cube):
	cube[[18, 19, 20, 27, 28, 29, 36, 37, 38, 9, 10, 11], :] = cube[[27, 28, 29, 36, 37, 38, 9, 10, 11, 18, 19, 20], :]
	return cube

def u_prime_move(cube):
	cube[[18, 19, 20, 27, 28, 29, 36, 37, 38, 9, 10, 11], :] = cube[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38], :]
	return cube

# FIX L MOVES
def l_move(cube):
    cube[[0, 3, 6, 18, 21, 24, 44, 47, 50, 38, 41, 43], :] = cube[[38, 41, 43, 0, 3, 6, 18, 21, 24, 44, 47, 50], :]
    return cube

def l_prime_move(cube):
    cube[[0, 3, 6, 18, 21, 24, 44, 47, 50, 38, 41, 43], :] = cube[[18, 21, 24, 44, 47, 50, 38, 41, 43, 0, 3, 6], :]
    return cube

def f_move(cube):
	pass

def f_prime_move(cube):
	pass

def r_move(cube):
	pass

def r_prime_move(cube):
	pass

def b_move(cube):
	pass

def b_prime_move(cube):
	pass

def d_move(cube):
	pass

def d_prime_move(cube):
	pass

print(cube[[41], :])

cube = l_move(cube)

for row in cube:
    face_index, _, _ = row
    color = colors[face_index]
    print(color)
