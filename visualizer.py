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

# Define vertices for a single cubie (slightly increased size)
vertices = [
    [-0.47, -0.47, -0.47], [0.47, -0.47, -0.47], [0.47, 0.47, -0.47], [-0.47, 0.47, -0.47],
    [-0.47, -0.47, 0.47], [0.47, -0.47, 0.47], [0.47, 0.47, 0.47], [-0.47, 0.47, 0.47]
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

# Draw a single cubie with specified colors for outer faces and black for inner faces
def draw_cubie(position, color_assignment, x, y, z):
    glPushMatrix()
    glTranslatef(*position)

    # Increase polygon offset to reduce z-fighting
    glEnable(GL_POLYGON_OFFSET_FILL)
    glPolygonOffset(2.0, 2.0)

    # Draw faces with colors
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        # Determine if the current face is an outer face
        if (i == 0 and z == -1) or (i == 1 and z == 1) or \
           (i == 2 and x == -1) or (i == 3 and x == 1) or \
           (i == 4 and y == -1) or (i == 5 and y == 1):
            glColor3fv(colors[color_assignment[i]])
        else:
            glColor3fv(colors['black'])  # Inner faces are black
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glDisable(GL_POLYGON_OFFSET_FILL)

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
                # Assign face colors for outer cubies, and black for inner cubies
                color_assignment = [
                    'blue' if z == -1 else 'green' if z == 1 else 'black',
                    'green' if z == 1 else 'blue' if z == -1 else 'black',
                    'orange' if x == -1 else 'red' if x == 1 else 'black',
                    'red' if x == 1 else 'orange' if x == -1 else 'black',
                    'yellow' if y == -1 else 'white' if y == 1 else 'black',
                    'white' if y == 1 else 'yellow' if y == -1 else 'black'
                ]
                rubiks_cube.append(((x, y, z), color_assignment, x, y, z))
    return rubiks_cube

# Main function
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -15)

    # Enable depth testing
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)

    rubiks_cube = create_rubiks_cube()

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
				quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 3, 1, 1)

        # Draw each cubie in the Rubik's Cube
        for position, color_assignment, x, y, z in rubiks_cube:
            draw_cubie(position, color_assignment, x, y, z)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
