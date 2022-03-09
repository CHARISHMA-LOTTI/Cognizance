import numpy as np
given_vector = np.array([10,11,12,13,14])
msg = f'given vector = {given_vector}'
print(msg)
final_vector = np.zeros(len(given_vector) + (len(given_vector)-1)*5)
final_vector[::6] = given_vector
fin = f'final vector = {final_vector}'
print(fin)