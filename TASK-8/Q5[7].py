import numpy as np
array1 = np.array([1,2,3,4,5,6,12,7,20])
array2 = np.array([3,2,5,4,11,5,0,8,20])
print("the indices where the elements of 2 arrays match are :")
for i in range(9):
  if array1[i] == array2[i]:
    print(i)

