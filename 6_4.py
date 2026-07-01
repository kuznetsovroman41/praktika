import numpy as np

my_list = np.array([True, 5, 'go', 3 + 0.1j], dtype=object)

my_list = np.roll(my_list, 1)
print("После сдвига:", my_list)