import numpy as np

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(F"The arrary is created with array function: {arr1}\n")

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

print(F"The Nested sequences is created with array function:\n {arr2}\n")
print(f"The dimensions of array is: {arr2.ndim}\n")
print(f"The Shape of array is: {arr2.shape}\n")
print(f"The Data type of array is: {arr2.dtype}\n")

info = """, there are a number of other functions for creating new
arrays. As examples, zeros and ones create arrays of 0s or 1s, respectively, with a
given length or shape. \n"""

print(info)

zeros = np.zeros(10)
print(F"The Zeros array is created with zeros() function: {zeros}\n")

zeros_w_tuple = np.zeros((3, 6))
print(F"The Zeros array is created with zeros() function having tuple: \n{zeros_w_tuple}\n")

ones = np.ones(10)
print(F"The Ones array is created with ones() function: {ones}\n")

ones_w_tuple = np.ones((3, 6))
print(F"The Ones array is created with ones() function having tuple: \n{ones_w_tuple}\n")

empty = np.empty((2, 3, 5))
print(F"The empty array is created with zeros() function:\n {empty}\n")

arrange = np.arange(15)
print(F"The arrange array is created with arange() function: {arrange}\n")


