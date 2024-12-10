from solver.movements import Uturn, Uprime, U2, Dturn, Dprime, D2, Fturn, Fprime, F2, Rturn, Rprime, R2, Lturn, Lprime, L2, Bturn, Bprime, B2
from collections import deque
import time

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

    # BFS setup
    queue = deque()
    queue.append((cube, [], 0))  # (current cube state, move sequence, depth)
    visited = set()

    start_time = time.time()

    # BFS loop
    while queue:
        current_cube, move_sequence, depth = queue.popleft()

        # Check if white cross is solved
        if is_white_cross_solved(current_cube):
            # Apply the solution to the original cube
            for move in move_sequence:
                move(cube)

            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Execution Time: {execution_time:.4f} seconds")

            return [move_names[move] for move in move_sequence]

        # If depth exceeds 8, stop exploring further
        if depth >= 8:
            continue

        # Generate new states for all possible moves
        for move in moves:
            # Create a deep copy of the cube
            temp_cube = {k: [row.copy() for row in v] for k, v in current_cube.items()}
            move(temp_cube)

            # Serialize the state to a tuple for the visited check
            state_tuple = tuple(tuple(row) for face in temp_cube.values() for row in face)
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((temp_cube, move_sequence + [move], depth + 1))

    return None  # Return None if no solution found under 8 moves
