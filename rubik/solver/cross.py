from solver.movements import Uturn, Uprime, U2, Dturn, Dprime, D2, Fturn, Fprime, F2, Rturn, Rprime, R2, Lturn, Lprime, L2, Bturn, Bprime, B2

def solve_white_cross(cube):
    """
    Solve the white cross on any scrambled cube in 8 moves or less.
    """
    # Helper function to check if the white cross is solved
    def is_white_cross_solved(cube):
        """
        Check if the white cross is solved and the edges are aligned with the side centers.
        """
        return (
            cube['U'][0][1][0] == 'W' and cube['F'][0][1][0] == cube['F'][1][1][0] and  # UF Edge
            cube['U'][1][2][0] == 'W' and cube['R'][0][1][0] == cube['R'][1][1][0] and  # UR Edge
            cube['U'][2][1][0] == 'W' and cube['B'][0][1][0] == cube['B'][1][1][0] and  # UB Edge
            cube['U'][1][0][0] == 'W' and cube['L'][0][1][0] == cube['L'][1][1][0]      # UL Edge
        )


    # Possible moves to try
    moves = [
        Uturn, Uprime, U2,
        Dturn, Dprime, D2,
        Fturn, Fprime, F2,
        Rturn, Rprime, R2,
        Lturn, Lprime, L2,
        Bturn, Bprime, B2
    ]

    # To display move names for readability
    move_names = {
        Uturn: "U", Uprime: "U'", U2: "U2",
        Dturn: "D", Dprime: "D'", D2: "D2",
        Fturn: "F", Fprime: "F'", F2: "F2",
        Rturn: "R", Rprime: "R'", R2: "R2",
        Lturn: "L", Lprime: "L'", L2: "L2",
        Bturn: "B", Bprime: "B'", B2: "B2"
    }

    # Try solving with move sequences of increasing lengths
    from itertools import product

    for num_moves in range(1, 9):  # Up to 8 moves
        for move_sequence in product(moves, repeat=num_moves):
            # Create a temporary copy of the cube
            temp_cube = {k: [row.copy() for row in v] for k, v in cube.items()}

            # Apply the moves to the temporary cube
            for move in move_sequence:
                move(temp_cube)

            # Check if the white cross is solved
            if is_white_cross_solved(temp_cube):
                # Return the sequence of moves in readable format
                [move(cube) for move in move_sequence]
                return [move_names[move] for move in move_sequence]

    return None  # Return None if no solution found within 8 moves
