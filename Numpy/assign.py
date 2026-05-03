import numpy as np

# First to create array

full_array = np.array([5,10,15,20,25,30])
# Print Full Array
print(full_array)
# Print First Element
print(full_array[0])
# Print Last Element
print(full_array[5])
# Slice Element from one to four
print(full_array[1:4])
# Find Mean of the Array
print(np.mean(full_array))
# Find Sum of full array
print(np.sum(full_array))
# Find Maximum Value from the array
print(np.max(full_array))
# Multiply array with three
print(full_array*3)
# print value greater than 18
print(full_array[full_array>18])


new_array = np.array([[7,8],
 [9,10],
 [11,12]])
print(new_array)
