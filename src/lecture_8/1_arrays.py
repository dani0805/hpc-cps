import numpy as np

# 8.3.1 Array Creation
array_1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Array 1:\n", array_1)

# 8.3.2 Basic Operations
array_2 = array_1 * 2.0
print("\nArray 2:\n", array_2)

# 8.3.3 Indexing, Slicing and Iterating
print("\nIndexing:\n", array_2[1, 2])  # Element at second row, third column
print("Slicing:\n", array_2[0, :])
# array_2[0, :] is equivalent to array_2[0]
# First row
for row in array_2:
    print("Iterating:\n", row)

# 8.3.4 Broadcasting with Numbers
array_3 = array_1 + 1
print("\nBroadcasting with Numbers:\n", array_3)

# 8.3.5 Broadcasting of Functions
array_4 = np.sqrt(array_1)
print("\nBroadcasting of Functions:\n", array_4)

# 8.3.6 Aggregation Along an Axis
print("\nSum Along an Axis:\n", np.sum(array_1, axis=0))

# 8.3.7 Reshaping Arrays
array_5 = array_1.reshape(3, 2)
# array_5 = np.array([
#     [1, 2],
#     [3, 4]
#     [5, 6]
# ])
print("\nReshaped Array:\n", array_5)

# 8.3.8 Joining Arrays
array_6 = np.concatenate((array_1, array_2), axis=0)
print("\nJoined Array:\n", array_6)

# 8.3.9 Stacking Arrays
array_7 = np.hstack((array_1, array_2))
print("\nStacked Array:\n", array_7)

# 8.3.10 Splitting Arrays
array_8, array_9, array_10 = np.hsplit(array_6, 3)
print("\nSplit Arrays:\n", array_8, "\n", array_9, "\n", array_10)
