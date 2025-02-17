import numpy as np
data = np.random.randn(2, 3)
print(f"Random data: {data}\n")

print(f"Addition: {data+data}\n")
print(f"Subraction: {data-data}\n")
print(f"Multiplication: {data*10}\n")
print(f"Division: {data/10}\n")

print(f"The shape of arrary is: {data.shape}\n")
print(f"The data type of arrary is: {data.dtype}")