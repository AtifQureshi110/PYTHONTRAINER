my_list = [1, 2, 3, 4, 5]
print("this is the original list.\n",my_list)
# Remove a specific element
my_list.remove(3)
print("the remove()will remove item 3 from the list.\n",my_list) 

# Remove by index
my_list.pop(1)
print("the pop(1) will remove item at index 1 from the list \n",my_list)   

# Remove the last element
my_list.pop()
print("the pop() will be from remove at end of the list\n",my_list) 

# Clear the list
my_list.clear()
print("the clear() will clear the existing list with all items.\n",my_list) 
