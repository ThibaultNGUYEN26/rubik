def rotate_face(face_matrix, direction):
    if direction == 'clockwise':
        return [list(row) for row in zip(*face_matrix[::-1])]
    elif direction == 'counterclockwise':
        return [list(row) for row in zip(*face_matrix)][::-1]
    elif direction == '180':
        return [row[::-1] for row in face_matrix[::-1]]


def Uturn(cube):
    # Rotate the U face clockwise
    cube['U'] = rotate_face(cube['U'], 'clockwise')

    # Update the adjacent edges: F, R, B, L
    temp = cube['F'][0].copy()
    cube['F'][0] = cube['R'][0]
    cube['R'][0] = cube['B'][0]
    cube['B'][0] = cube['L'][0]
    cube['L'][0] = temp


def Uprime(cube):
    # Rotate the U face counterclockwise
    cube['U'] = rotate_face(cube['U'], 'counterclockwise')

    # Update the adjacent edges: F, L, B, R
    temp = cube['F'][0].copy()
    cube['F'][0] = cube['L'][0]
    cube['L'][0] = cube['B'][0]
    cube['B'][0] = cube['R'][0]
    cube['R'][0] = temp


def U2(cube):
    Uturn(cube)
    Uturn(cube)


def Dturn(cube):
    # Rotate the D face clockwise
    cube['D'] = rotate_face(cube['D'], 'clockwise')

    # Update the adjacent edges: F, L, B, R
    temp = cube['F'][2].copy()
    cube['F'][2] = cube['L'][2]
    cube['L'][2] = cube['B'][2]
    cube['B'][2] = cube['R'][2]
    cube['R'][2] = temp


def Dprime(cube):
    # Rotate the D face counterclockwise
    cube['D'] = rotate_face(cube['D'], 'counterclockwise')

    # Update the adjacent edges: F, R, B, L
    temp = cube['F'][2].copy()
    cube['F'][2] = cube['R'][2]
    cube['R'][2] = cube['B'][2]
    cube['B'][2] = cube['L'][2]
    cube['L'][2] = temp


def D2(cube):
    Dturn(cube)
    Dturn(cube)


def Fturn(cube):
    # Rotate the F face clockwise
    cube['F'] = rotate_face(cube['F'], 'clockwise')

    # Update the adjacent edges: U, R, D, L
    temp = cube['U'][2].copy()
    cube['U'][2][0], cube['U'][2][1], cube['U'][2][2] = cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]
    cube['L'][0][2], cube['L'][1][2], cube['L'][2][2] = cube['D'][0][0], cube['D'][0][1], cube['D'][0][2]
    cube['D'][0][0], cube['D'][0][1], cube['D'][0][2] = cube['R'][2][0], cube['R'][1][0], cube['R'][0][0]
    cube['R'][0][0], cube['R'][1][0], cube['R'][2][0] = temp


def Fprime(cube):
    # Rotate the F face counterclockwise
    cube['F'] = rotate_face(cube['F'], 'counterclockwise')

    # Update the adjacent edges: U, L, D, R
    temp = cube['U'][2].copy()
    cube['U'][2][0], cube['U'][2][1], cube['U'][2][2] = cube['R'][0][0], cube['R'][1][0], cube['R'][2][0]
    cube['R'][0][0], cube['R'][1][0], cube['R'][2][0] = cube['D'][0][2], cube['D'][0][1], cube['D'][0][0]
    cube['D'][0][0], cube['D'][0][1], cube['D'][0][2] = cube['L'][2][2], cube['L'][1][2], cube['L'][0][2]
    cube['L'][0][2], cube['L'][1][2], cube['L'][2][2] = temp


def F2(cube):
    Fturn(cube)
    Fturn(cube)


def Lturn(cube):
    # Rotate the L face clockwise
    cube['L'] = rotate_face(cube['L'], 'clockwise')

    # Update adjacent edges: U, F, D, B
    temp = [cube['U'][0][0], cube['U'][1][0], cube['U'][2][0]]
    cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]
    cube['B'][0][2], cube['B'][1][2], cube['B'][2][2] = cube['D'][2][0], cube['D'][1][0], cube['D'][0][0]
    cube['D'][0][0], cube['D'][1][0], cube['D'][2][0] = cube['F'][0][0], cube['F'][1][0], cube['F'][2][0]
    cube['F'][0][0], cube['F'][1][0], cube['F'][2][0] = temp[::-1]


def Lprime(cube):
    # Rotate the L face counterclockwise
    cube['L'] = rotate_face(cube['L'], 'counterclockwise')

    # Update adjacent edges: U, B, D, F
    temp = [cube['U'][0][0], cube['U'][1][0], cube['U'][2][0]]
    cube['U'][0][0], cube['U'][1][0], cube['U'][2][0] = cube['F'][0][0], cube['F'][1][0], cube['F'][2][0]
    cube['F'][0][0], cube['F'][1][0], cube['F'][2][0] = cube['D'][0][0], cube['D'][1][0], cube['D'][2][0]
    cube['D'][0][0], cube['D'][1][0], cube['D'][2][0] = cube['B'][2][2], cube['B'][1][2], cube['B'][0][2]
    cube['B'][0][2], cube['B'][1][2], cube['B'][2][2] = temp[::-1]


def L2(cube):
    Lturn(cube)
    Lturn(cube)


def Rturn(cube):
    # Rotate the R face clockwise
    cube['R'] = rotate_face(cube['R'], 'clockwise')

    # Update adjacent edges: U, F, D, B
    temp = [cube['U'][0][2], cube['U'][1][2], cube['U'][2][2]]
    cube['U'][0][2], cube['U'][1][2], cube['U'][2][2] = cube['F'][0][2], cube['F'][1][2], cube['F'][2][2]
    cube['F'][0][2], cube['F'][1][2], cube['F'][2][2] = cube['D'][0][2], cube['D'][1][2], cube['D'][2][2]
    cube['D'][0][2], cube['D'][1][2], cube['D'][2][2] = cube['B'][2][0], cube['B'][1][0], cube['B'][0][0]
    cube['B'][0][0], cube['B'][1][0], cube['B'][2][0] = temp[::-1]


def Rprime(cube):
    # Rotate the R face counterclockwise
    cube['R'] = rotate_face(cube['R'], 'counterclockwise')

    # Update adjacent edges: U, B, D, F
    temp = [cube['U'][0][2], cube['U'][1][2], cube['U'][2][2]]
    cube['U'][0][2], cube['U'][1][2], cube['U'][2][2] = cube['B'][0][0], cube['B'][1][0], cube['B'][2][0]
    cube['B'][0][0], cube['B'][1][0], cube['B'][2][0] = cube['D'][2][2], cube['D'][1][2], cube['D'][0][2]
    cube['D'][0][2], cube['D'][1][2], cube['D'][2][2] = cube['F'][0][2], cube['F'][1][2], cube['F'][2][2]
    cube['F'][0][2], cube['F'][1][2], cube['F'][2][2] = temp


def R2(cube):
    Rturn(cube)
    Rturn(cube)


def Bturn(cube):
    # Rotate the B face clockwise
    cube['B'] = rotate_face(cube['B'], 'clockwise')

    # Update the adjacent edges: U, R, D, L
    temp = cube['U'][0].copy()
    cube['U'][0][0], cube['U'][0][1], cube['U'][0][2] = cube['R'][0][2], cube['R'][1][2], cube['R'][2][2]
    cube['R'][0][2], cube['R'][1][2], cube['R'][2][2] = cube['D'][2][2], cube['D'][2][1], cube['D'][2][0]
    cube['D'][2][0], cube['D'][2][1], cube['D'][2][2] = cube['L'][2][0], cube['L'][1][0], cube['L'][0][0]
    cube['L'][0][0], cube['L'][1][0], cube['L'][2][0] = temp[::-1]


def Bprime(cube):
    # Rotate the B face counterclockwise
    cube['B'] = rotate_face(cube['B'], 'counterclockwise')

    # Update the adjacent edges: U, L, D, R
    temp = cube['U'][0].copy()
    cube['U'][0][0], cube['U'][0][1], cube['U'][0][2] = cube['L'][0][0], cube['L'][1][0], cube['L'][2][0]
    cube['L'][0][0], cube['L'][1][0], cube['L'][2][0] = cube['D'][2][0], cube['D'][2][1], cube['D'][2][2]
    cube['D'][2][0], cube['D'][2][1], cube['D'][2][2] = cube['R'][2][2], cube['R'][1][2], cube['R'][0][2]
    cube['R'][0][2], cube['R'][1][2], cube['R'][2][2] = temp[::-1]


def B2(cube):
    Bturn(cube)
    Bturn(cube)
