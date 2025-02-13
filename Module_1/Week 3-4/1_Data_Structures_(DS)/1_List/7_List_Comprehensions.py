# Create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# # simnplification od above code 
# squares=[] # empty list
# for x in range(1, 11): # for loop 
#     output=x**2
#     squares.append(output)
# print(squares)

# Filter even numbers from a list
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]

# # simnplification od above code 
# even_numbers = [] # empty
# for x in range(10): # for loop
#     if x % 2 == 0: # condition
#         even_numbers.append(x)
# print(even_numbers)