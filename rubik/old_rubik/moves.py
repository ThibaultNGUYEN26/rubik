def u_move(cube):
	cube[[18, 19, 20, 27, 28, 29, 36, 37, 38, 9, 10, 11, 0, 1, 2, 3, 5, 6, 7, 8], :] = cube[[27, 28, 29, 36, 37, 38, 9, 10, 11, 18, 19, 20, 6, 3, 0, 7, 1, 8, 5, 2], :]
	return cube

def u_prime_move(cube):
	cube[[18, 19, 20, 27, 28, 29, 36, 37, 38, 9, 10, 11, 0, 1, 2, 3, 5, 6, 7, 8], :] = cube[[9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 2, 5, 8, 1, 7, 0, 3, 6], :]
	return cube

def l_move(cube):
	cube[[0, 3, 6, 18, 21, 24, 45, 48, 51, 38, 41, 44, 9, 10, 11, 12, 14, 15, 16, 17], :] = cube[[44, 41, 38, 0, 3, 6, 18, 21, 24, 51, 48, 45, 15, 12, 9, 16, 10, 17, 14, 11], :]
	return cube

def l_prime_move(cube):
	cube[[0, 3, 6, 18, 21, 24, 45, 48, 51, 38, 41, 44, 9, 10, 11, 12, 14, 15, 16, 17], :] = cube[[18, 21, 24, 45, 48, 51, 44, 41, 38, 6, 3, 0, 11, 14, 17, 10, 16, 9, 12, 15], :]
	return cube

def f_move(cube):
	cube[[6, 7, 8, 27, 30, 33, 45, 46, 47, 11, 14, 17, 18, 19, 20, 21, 23, 24, 25, 26], :] = cube[[17, 14, 11, 6, 7, 8, 33, 30, 27, 45, 46, 47, 24, 21, 18, 25, 19, 26, 23, 20], :]
	return cube

def f_prime_move(cube):
	cube[[6, 7, 8, 27, 30, 33, 45, 46, 47, 11, 14, 17, 18, 19, 20, 21, 23, 24, 25, 26], :] = cube[[27, 30, 33, 47, 46, 45, 11, 14, 17, 8, 7, 6, 20, 23, 26, 19, 25, 18, 21, 24], :]
	return cube

def r_move(cube):
	cube[[2, 5, 8, 20, 23, 26, 47, 50, 53, 36, 39, 42, 27, 28, 29, 30, 32, 33, 34, 35], :] = cube[[20, 23, 26, 47, 50, 53, 42, 39, 36, 8, 5, 2, 33, 30, 27, 34, 28, 35, 32, 29], :]
	return cube

def r_prime_move(cube):
	cube[[2, 5, 8, 20, 23, 26, 47, 50, 53, 36, 39, 42, 27, 28, 29, 30, 32, 33, 34, 35], :] = cube[[42, 39, 36, 2, 5, 8, 20, 23, 26, 53, 50, 47, 29, 32, 35, 28, 34, 27, 30, 33], :]
	return cube

def b_move(cube):
	cube[[0, 1, 2, 29, 32, 35, 51, 52, 53, 9, 12, 15, 36, 37, 38, 39, 41, 42, 43, 44], :] = cube[[29, 32, 35, 53, 52, 51, 9, 12, 15, 2, 1, 0, 42, 39, 36, 43, 37, 44, 41, 38], :]
	return cube

def b_prime_move(cube):
	cube[[0, 1, 2, 29, 32, 35, 51, 52, 53, 9, 12, 15, 36, 37, 38, 39, 41, 42, 43, 44], :] = cube[[15, 12, 9, 0, 1, 2, 35, 32, 29, 51, 52, 53, 38, 41, 44, 37, 43, 36, 39, 42], :]
	return cube

def d_move(cube):
	cube[[24, 25, 26, 33, 34, 35, 42, 43, 44, 15, 16, 17, 45, 46, 47, 48, 50, 51, 52, 53], :] = cube[[15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 48, 45, 52, 46, 53, 50, 47], :]
	return cube

def d_prime_move(cube):
	cube[[24, 25, 26, 33, 34, 35, 42, 43, 44, 15, 16, 17, 45, 46, 47, 48, 50, 51, 52, 53], :] = cube[[33, 34, 35, 42, 43, 44, 15, 16, 17, 24, 25, 26, 47, 50, 53, 46, 52, 45, 48, 51], :]
	return cube