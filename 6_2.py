import numpy as np

A = np.array([int(input()) for _ in range(10)])
B = np.array([int(input()) for _ in range(10)])

A, B = B, A

print("Новый A:", A)
print("Новый B:", B)