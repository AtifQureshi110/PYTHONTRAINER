nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)  

# nested_list = [[1, 2], [3, 4], [5, 6]]
# flat_list=[]
# for sublist in nested_list:
#     for item in sublist:
#         flat_list.append(item)
# print(flat_list)