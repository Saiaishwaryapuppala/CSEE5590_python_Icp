import numpy as np
x = np.random.random(20)
print("original array:")
print(x)
b= x.reshape((4, 5))
index_array = np.argmax(b, axis=1)
print(b)

b[0][index_array[0]] = 0
b[1][index_array[0]] = 1
b[2][index_array[0]] = 2
b[3][index_array[0]] = 3

print("max value replaced by 0:")
print(b)
