import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define colors for Rubik's Cube (WCA color scheme)
colors = {
    'white': (1, 1, 1),
    'yellow': (1, 1, 0),
    'red': (1, 0, 0),
    'orange': (1, 0.5, 0),
    'green': (0, 1, 0),
    'blue': (0, 0, 1),
    'black': (0, 0, 0)
}

# Define vertices for a single cubie (reduced size for tighter fit)
vertices = [
    [-0.48, -0.48, -0.48], [0.48, -0.48, -0.48], [0.48, 0.48, -0.48], [-0.48, 0.48, -0.48],
    [-0.48, -0.48, 0.48], [0.48, -0.48, 0.48], [0.48, 0.48, 0.48], [-0.48, 0.48, 0.48]
]

# Define faces of a cubie
faces = [
    (0, 1, 2, 3),  # Back face
    (4, 5, 6, 7),  # Front face
    (0, 3, 7, 4),  # Left face
    (1, 2, 6, 5),  # Right face
    (0, 1, 5, 4),  # Bottom face
    (3, 2, 6, 7)   # Top face
]

# Draw a single cubie with specified colors for each face and black borders
def draw_cubie(position, color_assignment):
    glPushMatrix()
    glTranslatef(*position)

    # Draw faces with colors
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[color_assignment[i]])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Draw black borders
    glColor3fv(colors['black'])
    glLineWidth(2)
    glBegin(GL_LINES)
    for edge in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    glPopMatrix()

# Create a 3x3x3 grid of cubies
def create_rubiks_cube():
    rubiks_cube = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                # Assign face colors based on position
                color_assignment = [
                    'blue' if z == -1 else 'green' if z == 1 else 'black',
                    'green' if z == 1 else 'blue' if z == -1 else 'black',
                    'orange' if x == -1 else 'red' if x == 1 else 'black',
                    'red' if x == 1 else 'orange' if x == -1 else 'black',
                    'yellow' if y == -1 else 'white' if y == 1 else 'black',
                    'white' if y == 1 else 'yellow' if y == -1 else 'black'
                ]
                rubiks_cube.append(((x, y, z), color_assignment))
    return rubiks_cube

# Main function
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    glEnable(GL_DEPTH_TEST)
    glDisable(GL_CULL_FACE)

    rubiks_cube = create_rubiks_cube()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        # Draw each cubie in the Rubik's Cube
        for position, color_assignment in rubiks_cube:
            draw_cubie((position[0] * 1.0, position[1] * 1.0, position[2] * 1.0), color_assignment)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
