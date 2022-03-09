import numpy as np
# the arrays vector1 and vector2 are given some dummy elements at first
vector1 = np.array([0, 0, 0, 0, 0])
i = 0
print("enter the elements of 1st vector")
while i <= 4:
  vector1[i] = input(": ")
  i +=1

vector2 = np.array([0, 0, 0, 0, 0])  
print("enter the elements of 2nd vector")
k = 0
while k <= 4:
  vector2[k] = input(": ")
  k +=1

print(np.allclose(vector1, vector2))