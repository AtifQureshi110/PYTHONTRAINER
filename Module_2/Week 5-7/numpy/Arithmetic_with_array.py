import numpy as np

info = """Arrays are important because they enable you to express batch operations on data
without writing any for loops. NumPy users call this vectorization. Any arithmetic
operations between equal-size arrays applies the operation element-wise:"""

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(f"A simple 2d array: \n{arr}\n")

print(f" the addition of arr: \n{arr+arr}\n")
print(f" the subraction of arr: \n{arr-arr}\n")
print(f" the multiplication of arr: \n{arr*arr}\n")
print(f" the subraction of arr: \n{arr-arr}\n")
print(f" the square of arr: \n{arr**2}\n")

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
print(f"A simple 2d array: \n{arr2}\n")

print(f"The comparision of two array: \n{arr2 > arr}\n")