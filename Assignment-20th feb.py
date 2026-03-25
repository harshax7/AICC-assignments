import time
import numpy as np

size = 1000000
py_list = list(range(size))
np_array = np.arange(size)

start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()
print("Python List Time:", end - start)
start = time.time()
np_result = np_array * 2
end = time.time()
print("NumPy Array Time:", end - start)

# output
# Python List Time: 0.25 seconds
# NumPy Array Time: 0.01 seconds