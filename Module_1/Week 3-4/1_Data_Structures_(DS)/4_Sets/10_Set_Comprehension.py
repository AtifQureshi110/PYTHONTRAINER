# Similar to list comprehensions, you can create sets using comprehensions.
squared_set = {x**2 for x in range(1, 6)}
print(squared_set) 


# To understand the Set_comprehension this is simplify version of above code 
# squared_set = { } # empty set
# for x in range(1, 6): # loop
#     squared_set.add(x**2) # adding item in the empty set
# print(squared_set) # result