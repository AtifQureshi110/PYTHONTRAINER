import numpy as np

info = """\nThe data type or dtype is a special object containing the information (or metadata,
data about data) the ndarray needs to interpret a chunk of memory as a particular
type of data \n"""

print (info)

arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype)
print("The data type of arr1 is float: ", arr1, '\n')


arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr2.dtype)
print("The data type of arr1 is int: ", arr2, '\n')


arr = np.array([1, 2, 3, 4, 5])
print(f"the dtype of array is integer: {arr, arr.dtype}\n")

float_arr = arr.astype(np.float64)
print(f"the dtype of arr is changed with astype(): {float_arr, float_arr.dtype}\n")

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(f"the dtype of array is integer: {arr, arr.dtype}\n")

int_arr = arr.astype(np.int32)
print(f"Dtype is change to integer: {int_arr}\n")

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.str_)
print(f"numeric_strings: {numeric_strings}")

string_float = numeric_strings.astype(float)
print(f"The string dtype is changed into float {string_float, string_float.dtype}")
