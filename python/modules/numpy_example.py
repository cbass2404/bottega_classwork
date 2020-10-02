import numpy as np

# generates an array of 0 through 15
num_range = np.arange(16)

num_range = num_range.reshape(2, 8)

num_range = num_range.reshape(4, 4)

print(num_range)
