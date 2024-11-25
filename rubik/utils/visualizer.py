from vpython import box, vector, rate, scene, color, compound, canvas, distant_light, local_light
import numpy as np
from threading import Lock
import re  # For regular expression parsing

def start_rubiks_visualizer(scramble_str):
    # Initialize the scene
    scene = canvas(
        background=vector(0.95, 0.95, 0.95),  # Light background
        width=1300,
        height=700,
        title="<b style='position: absolute; font-size: calc(1vw + 1vh); font-weight: bold; color: black; left: 50%; top: 5%; transform: translate(-50%, 0);'>Rubik's Cube Visualizer</b>",
        center=vector(0, 0, 0)
    )

    # Apply CSS styling to center the canvas
    scene.append_to_title("""
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
            overflow: hidden;
        }
        canvas {
            border: 2px solid black; /* Optional: Add border around the canvas */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.3); /* Optional: Add shadow for styling */
        }
    </style>
    """)

    # Add ambient light to illuminate the entire scene evenly
    scene.ambient = color.gray(0.1)  # Softer gray ambient light

    # Add directional lights
    distant_light(direction=vector(1, -1, -1), color=color.white)  # Light from top-right
    distant_light(direction=vector(-1, -1, -1), color=color.gray(0.5))  # Light from top-left
    distant_light(direction=vector(1, 1, 1), color=color.gray(0.3))  # Light from bottom-right

    # Define colors for each face
    face_colors = {
        'U': color.white,                   # Up (White)
        'D': vector(1, 1, 0),               # Down (Bright Yellow)
        'F': vector(0, 0.8, 0),             # Front (Bright Green)
        'B': vector(0, 0.4, 1),             # Back (Sky Blue)
        'L': vector(1, 0.55, 0),            # Left (Distinct Orange)
        'R': vector(1, 0, 0),               # Right (Bright Red)
    }

    # Offset to center the Rubik's Cube at the origin
    offset = -1

    # Create a dictionary to hold all the smaller cubes with their positions as keys
    cubes = {}

    # Lock for handling animation spamming
    animation_lock = Lock()

    # Track the key state to prevent repeated actions
    key_state = {}

    # Function to create a single cubie with colored faces
    def create_cubie(x, y, z):
        scale = 0.1  # Smaller scale factor for the entire cube
        cubie = box(
            pos=vector((x + offset) * scale, (y + offset) * scale, (z + offset) * scale),  # Scaled position
            size=vector(0.95 * scale, 0.95 * scale, 0.95 * scale),  # Scaled size
            color=color.black,
            shininess=0.6  # Make it slightly shiny
        )

        # Create faces with appropriate colors, scaled to match the cubie
        faces = []
        if y == 2:
            faces.append(box(
                pos=cubie.pos + vector(0, 0.49 * scale, 0),
                size=vector(0.95 * scale, 0.02 * scale, 0.95 * scale),
                color=face_colors['U']
            ))
        if y == 0:
            faces.append(box(
                pos=cubie.pos + vector(0, -0.49 * scale, 0),
                size=vector(0.95 * scale, 0.02 * scale, 0.95 * scale),
                color=face_colors['D']
            ))
        if z == 2:
            faces.append(box(
                pos=cubie.pos + vector(0, 0, 0.49 * scale),
                size=vector(0.95 * scale, 0.95 * scale, 0.02 * scale),
                color=face_colors['F']
            ))
        if z == 0:
            faces.append(box(
                pos=cubie.pos + vector(0, 0, -0.49 * scale),
                size=vector(0.95 * scale, 0.95 * scale, 0.02 * scale),
                color=face_colors['B']
            ))
        if x == 0:
            faces.append(box(
                pos=cubie.pos + vector(-0.49 * scale, 0, 0),
                size=vector(0.02 * scale, 0.95 * scale, 0.95 * scale),
                color=face_colors['L']
            ))
        if x == 2:
            faces.append(box(
                pos=cubie.pos + vector(0.49 * scale, 0, 0),
                size=vector(0.02 * scale, 0.95 * scale, 0.95 * scale),
                color=face_colors['R']
            ))

        # Group the cubie and its faces
        group = [cubie] + faces
        return compound(group)

    # Create the 3x3x3 grid of cubies
    for x in range(3):
        for y in range(3):
            for z in range(3):
                position = (x, y, z)
                cubie = create_cubie(x, y, z)
                cubes[position] = cubie

    # Function to rotate a face
    def rotate_face(face, direction, animate=True):
        if animate:
            if not animation_lock.acquire(blocking=False):  # Check if lock is available
                return  # If another animation is in progress, ignore key press

        try:
            # Define rotation parameters
            angle = (np.pi / 2) * direction  # 90 degrees in radians, direction determines clockwise or counterclockwise
            steps = 30  # Number of steps for the animation
            dt = 0.001  # Time between steps

            # Select the cubies to rotate and define the rotation axis and origin
            if face == 'U':
                layer = [pos for pos in cubes if pos[1] == 2]
                axis = vector(0, -1, 0)  # Rotate around the y-axis
                origin = vector(0, 0.2, 0)  # Scaled origin
            elif face == 'D':
                layer = [pos for pos in cubes if pos[1] == 0]
                axis = vector(0, 1, 0)  # Rotate around the y-axis
                origin = vector(0, -0.2, 0)  # Scaled origin
            elif face == 'F':
                layer = [pos for pos in cubes if pos[2] == 2]
                axis = vector(0, 0, -1)  # Rotate around the z-axis
                origin = vector(0, 0, 0.2)  # Scaled origin
            elif face == 'B':
                layer = [pos for pos in cubes if pos[2] == 0]
                axis = vector(0, 0, 1)  # Rotate around the z-axis
                origin = vector(0, 0, -0.2)  # Scaled origin
            elif face == 'L':
                layer = [pos for pos in cubes if pos[0] == 0]
                axis = vector(1, 0, 0)  # Rotate around the x-axis
                origin = vector(-0.2, 0, 0)  # Scaled origin
            elif face == 'R':
                layer = [pos for pos in cubes if pos[0] == 2]
                axis = vector(-1, 0, 0)  # Rotate around the x-axis
                origin = vector(0.2, 0, 0)  # Scaled origin
            else:
                return

            if animate:
                # Animate the rotation of the entire face
                for i in range(steps):
                    rate(1 / dt)
                    for pos in layer:
                        cubie = cubes[pos]
                        cubie.rotate(angle=angle / steps, axis=axis, origin=origin)
            else:
                # Instant rotation without animation
                for pos in layer:
                    cubie = cubes[pos]
                    cubie.rotate(angle=angle, axis=axis, origin=origin)

            # Recalculate the positions of cubies in the rotated layer
            new_positions = {}
            for pos in layer:
                cubie = cubes[pos]

                # Calculate the new position after rotation
                relative_pos = vector(pos[0] - 1, pos[1] - 1, pos[2] - 1)
                rotated_pos = relative_pos.rotate(angle=angle, axis=axis)
                new_pos = (round(rotated_pos.x + 1), round(rotated_pos.y + 1), round(rotated_pos.z + 1))

                # Map the new position
                new_positions[new_pos] = cubie

            # Update the cubes dictionary with the new positions
            for pos in layer:
                del cubes[pos]
            cubes.update(new_positions)
        finally:
            if animate:
                animation_lock.release()  # Always release the lock if animation was used

    # Mapping user keys to faces (user can only press 'R' or 'r')
    key_to_face = {
        'r': ('R', 1),   # R: Rotate right face clockwise
        "R": ('R', -1), # R': Rotate right face counterclockwise
        'u': ('U', 1),
        "U": ('U', -1),
        'f': ('F', 1),
        "F": ('F', -1),
        'l': ('L', 1),
        "L": ('L', -1),
        'd': ('D', 1),
        "D": ('D', -1),
        'b': ('B', 1),
        "B": ('B', -1),
    }

    # Mapping scramble moves to faces and directions
    move_to_face = {
        'R': ('R', 1),   # R: Rotate right face clockwise
        "R'": ('R', -1), # R': Rotate right face counterclockwise
        'U': ('U', 1),
        "U'": ('U', -1),
        'F': ('F', 1),
        "F'": ('F', -1),
        'L': ('L', 1),
        "L'": ('L', -1),
        'D': ('D', 1),
        "D'": ('D', -1),
        'B': ('B', 1),
        "B'": ('B', -1),
        'R2': ('R', 2),   # R2: Rotate right face 180 degrees
        'U2': ('U', 2),
        'F2': ('F', 2),
        'L2': ('L', 2),
        'D2': ('D', 2),
        'B2': ('B', 2),
    }

    # Function to parse the scramble string into moves
    def parse_scramble(scramble_str):
        # Use regular expressions to split the scramble string into moves
        tokens = re.findall(r"[URFDLB]2?'?", scramble_str)
        moves = []
        for token in tokens:
            if token in move_to_face:
                moves.append(token)
            else:
                print(f"Invalid move in scramble: {token}")
        return moves

    # Parse the scramble string into a list of moves
    scramble_moves = parse_scramble(scramble_str)

    # Apply the scramble before entering the main loop
    for move in scramble_moves:
        face, direction = move_to_face[move]
        # For double turns (e.g., 'R2'), apply the rotation twice
        if direction == 2:
            rotate_face(face, 1, animate=False)
            rotate_face(face, 1, animate=False)
        else:
            rotate_face(face, direction, animate=False)

    # Handle key press events
    def keydown_handler(evt):
        s = evt.key
        if s in key_to_face and not key_state.get(s, False):  # Only process if key is not already pressed
            key_state[s] = True
            face, direction = key_to_face[s]
            rotate_face(face, direction)

    # Handle key release events
    def keyup_handler(evt):
        s = evt.key
        if s in key_state:
            key_state[s] = False  # Mark the key as released

    # Bind the key input functions
    scene.bind('keydown', keydown_handler)
    scene.bind('keyup', keyup_handler)

    # Keep the scene open
    while True:
        rate(60)

