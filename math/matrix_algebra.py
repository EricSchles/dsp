# Matrix Algebra

import numpy as np

matrix_A = np.array([
                [1, 2, 3], 
                [2, 7, 4]])

matrix_B = np.array([
                [1, -1], 
                [0, 1]])

matrix_C = np.array([
                [5, -1], 
                [9, 1],
                [6, 0]])

matrix_D = np.array([
                [3, -2, -1], 
                [1, 2, 3]])

vector_u = np.array([[6, 2, -3, 5]])
vector_v = np.array([[3, 5, -1, 4]])
vector_w = np.array([[1],
                     [8],
                     [0],
                     [5]])

print ('1. Matrix Operations')
print('1.1 ' + str(matrix_A.shape))
print('1.2 ' + str(matrix_B.shape))
print('1.3 ' + str(matrix_C.shape))
print('1.4 ' + str(matrix_D.shape))
print('1.5 ' + str(vector_u.shape))
print('1.6 ' + str(vector_w.shape))
print('\n')

alpha = 6

print ('2. Vector Operations')
print('2.1) ' + str(vector_u + vector_v))
print('2.2) ' + str(vector_u - vector_v))
print('2.3) ' + str(alpha*vector_u))
print('2.4) ' + str(np.vdot(vector_u,vector_v)))
print('2.5) ' + str(np.linalg.norm(vector_u)))
print('\n')

print ('3. Vector Operations')
# print('3.1) ' + str(matrix_A + matrix_C))
print('3.1) ' + 'not defined')
print('3.2) ' + str(matrix_A - matrix_C.T))
print('3.3) ' + str(matrix_C.T + 3*matrix_D))
print('3.4) ' + str(np.dot(matrix_B,matrix_A)))
# print('3.5) ' + str(np.dot(matrix_B,matrix_A.T)))
print('3.5) ' + 'not defined')
print('\n')

print ('Optional')
# print('3.6)' + str(np.dot(matrix_B,matrix_C)))
print('3.6) ' + 'not defined')
print('3.7) ' + str(np.dot(matrix_C,matrix_B)))
print('3.8) ' + str(np.power(matrix_B,4)))
print('3.9) ' + str(np.dot(matrix_A,matrix_A.T)))
print('3.10) ' + str(np.dot(matrix_D.T,matrix_D)))

# ANSWERS

# 1. Matrix Operations
# 1.1 (2, 3)
# 1.2 (2, 2)
# 1.3 (3, 2)
# 1.4 (2, 3)
# 1.5 (1, 4)
# 1.6 (4, 1)


# 2. Vector Operations
# 2.1) [[ 9  7 -4  9]]
# 2.2) [[ 3 -3 -2  1]]
# 2.3) [[ 36  12 -18  30]]
# 2.4) 51
# 2.5) 8.60232526704


# 3. Vector Operations
# 3.1) not defined
# 3.2) [[-4 -7 -3]
#  [ 3  6  4]]
# 3.3) [[14  3  3]
#  [ 2  7  9]]
# 3.4) [[-1 -5 -1]
#  [ 2  7  4]]
# 3.5) not defined


# Optional
# 3.6) not defined
# 3.7) [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]
# 3.8) [[1 1]
#  [0 1]]
# 3.9) [[14 28]
#  [28 69]]
# 3.10) [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]
