# -*- coding: utf-8 -*-
"""
Task 1 - Closures
Make a nested function and a python closure to make functions to get multiple multiplication functions using closures. That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.
"""

def multiplier_of(n):
  def multiplier(n2):
    return n2*n
  return multiplier

# test code
multiply_with_5 = multiplier_of(5)
print(multiply_with_5(9))
# should return 45

multiply_with_45 = multiplier_of(multiply_with_5(9))
print(multiply_with_45(2))
# should return: 90

"""Task 2 - decorators with arguments
Make a decorator factory which returns a decorator that decorates functions with one argument. The factory should take one argument, a type, and then returns a decorator that makes function should check if the input is the correct type. If it is wrong, it should print(“Bad Type”) (In reality, it should raise an error, but error raising isn’t in this tutorial). Look at the tutorial code and expected output to see what it is if you are confused (I know I would be.) Using isinstance(object, type_of_object) or type(object) might help.
"""

def type_check(correct_type):
  def check(old_function):
    def new_function(arg):
      if (isinstance(arg, correct_type)):
        return old_function(arg)
      else:
        print("Bad Type")
    return new_function
  return check
  
# Use  isinstance(arg, correct_type) to check if arg is of correct type

@type_check(int)
def times2(num):
  return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])

#Should produce:
#4
#Bad Type
#H
#Bad Type

"""Task 3 - Registering Plugins
Decorators don’t have to wrap the function they’re decorating. They can also simply register that a function exists and return it unwrapped. This can be used, for instance, to create a light-weight plug-in architecture:
"""

import random
PLUGINS = dict()

def register(func):
  PLUGINS[func.__name__] = func
  return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)
  
randomly_greet('John')

"""Task 4 - NumPy Exercises
Now that we’ve learned about NumPy let’s test your knowledge. We’ll start off with a few simple tasks, and then you’ll be asked some more complicated questions.
"""

#Import NumPy as np

import numpy as np

#Create an array of 10 zeros
#array([ 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

arr1 = np.zeros(10)
print(arr1)

#Create an array of 10 ones
#array([ 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])

arr2 = np.ones(10)
print(arr2)

#Create an array of 10 fives
#array([ 5., 5., 5., 5., 5., 5., 5., 5., 5., 5.])

arr3 = 5 * np.ones(10)
print(arr3)

#Create an array of integers from 10 to 50
#array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])

arr4 = range(10, 51) * np.ones(41)
print(arr4)

#Create an array of all the even integers from 10 to 50
#array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])

arr5 = range(10, 51, 2) * np.ones(21)
print(arr5)

#Create a 3x3 matrix with values ranging from 0 to 8
#array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

arr6 =  np.arange(0, 9).reshape(3,3)
print(arr6)

#Create a 3x3 identity matrix
#array([[ 1., 0., 0.], [ 0., 1., 0.], [ 0., 0., 1.]])

arr7 = np.identity(3)
print(arr7)

#Use NumPy to generate a random number between 0 and 1
#array([ 0.42829726])

rn = np.random.uniform(0, 1)
print(rn)                    


#Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
#"""array([ 1.32031013,  1.6798602 , -0.42985892, -1.53116655,  0.85753232,
#        0.87339938,  0.35668636, -1.47491157,  0.15349697,  0.99530727,
#       -0.94865451, -1.69174783,  1.57525349, -0.70615234,  0.10991879,
#       -0.49478947,  1.08279872,  0.76488333, -2.3039931 ,  0.35401124,
#       -0.45454399, -0.64754649, -0.29391671,  0.02339861,  0.38272124])"""

arr8 = np.random.normal(0, 1, 25)
print(arr8)

#Create the following matrix:
#"""array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
#       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
#       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
#       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
#       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
#       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
#       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
#       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
#       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
#       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])"""

arr9 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print(arr9)

#Create an array of 20 linearly spaced points between 0 and 1:
#"""array([ 0.        ,  0.05263158,  0.10526316,  0.15789474,  0.21052632,
#        0.26315789,  0.31578947,  0.36842105,  0.42105263,  0.47368421,
#        0.52631579,  0.57894737,  0.63157895,  0.68421053,  0.73684211,
#        0.78947368,  0.84210526,  0.89473684,  0.94736842,  1.        ])"""

arr10 = np.linspace(0, 1, 20)
print(arr10)

#Numpy Indexing and Selection
#Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

mat = np.arange(1,26).reshape(5,5)
#mat

#array([[ 1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10],
#       [11, 12, 13, 14, 15],
#       [16, 17, 18, 19, 20],
#       [21, 22, 23, 24, 25]])"""
#WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW

#a)
#array([[12, 13, 14, 15], [17, 18, 19, 20], [22, 23, 24, 25]])

arr_a = mat[2:, 1:]
print(arr_a)

#b)
#20 

arr_b = mat[3,4]
print(arr_b)

#c)
#array([[ 2], [ 7], [12]]) 

arr_c = mat[0:3,1]
print(arr_c)


#d)
#array([21, 22, 23, 24, 25]) 

arr_d = mat[4]
print(arr_d)

#e)
#array([[16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) 

arr_e = mat[3:]
print(arr_e)

#Now do the following
#Get the sum of all the values in mat
#325

sum = np.sum(mat)
print(sum)

#Get the standard deviation of the values in mat
#7.2111025509279782

std_dev=np.std(mat)
print(std_dev)

#Get the sum of all the columns in mat
#array([55, 60, 65, 70, 75])

arr_sum = mat.sum(axis=0)
print(arr_sum)

#Find median values in all columns
#[11. 12. 13. 14. 15.]

arr_med_col = np.median(mat, 0)
print(arr_med_col)

#Find average values in all columns
#‘[11. 12. 13. 14. 15.]’

arr_avg_col = np.mean(mat, 0)
print(arr_avg_col)

#Find median values in all rows
#[ 3. 8. 13. 18. 23.]

arr_med_row = np.median(mat, 1)
print(arr_med_row)

#Find average values in all rows
#[ 3. 8. 13. 18. 23.]

arr_avg_row = np.mean(mat, 1)
print(arr_avg_row)

"""Task 6 - Implement a Gaussian elimination algorithm with a function taking two arguments: A - the matrix, b - right hand side vector
A⋅x=b
Inside gaussian function you should create a copy of original matrix A, and create an augmented matrix of the form:
"""

#Aaug=[Ab]

def gaussian(A,b):
  for p_row in range(len(A)-1):
    for row in range(p_row+1, len(A)):
      multi = A[row][p_row]/A[p_row][p_row]
      for col in range(p_row + 1, len(A)):
        A[row][col] = A[row][col] - multi*A[p_row][col]
      b[row] = b[row] - multi*b[p_row]
  A = np.matrix(A)
  A = np.triu(A)
  b = np.transpose(np.matrix(b))
  A_aug = np.append(A, b, 1)
  return A_aug

A = np.arange(1, 17, dtype=np.float64).reshape(4,4)
b = A  @ x.T
gaussian(A1, b)

"""Task 7 - Implement a backward substitution and find a solution"""

A = np.arange(1, 17, dtype=np.float64).reshape(4,4)
A[1,2] = 88
A[1,3] = -3
A[2,3] = -3
print(f'A = {A}')

x = np.ones(A.shape[0])
print(f'Original x = {x}')
b = A  @ x.T
print(f'Right hand side for testing: b = {b}')


Ae = gaussian4(A, b)
print(f'Check if A was unchanged ')
print(f'Eliminated augmented matrix:\n {Ae}')
print(f'Eliminated augmented matrix A part: \n {Ae[:,:-1]}')
print(f'Eliminated augmented matrix b part: \n {Ae[:,Ae.shape[1]-1]}')

def back(A, b):
  x = np.zeros(A.shape[0])
  k = A.shape[0]-1
  x[k] = b[k]/A[k,k]
  while k >= 0:
    x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    k = k-1
  return x

# Find solution
x = back(Ae[:,:-1],Ae[:,Ae.shape[1]-1])
print(f'Solution: {x}')