import numpy as np

arrays = np.array(([1,2], [2,4], [-1,1/2], [-3,2], [2,3], [9,8], [-8,-9]))
l = []
for i in range(arrays.shape[0]):
    for j in range(arrays.shape[0]):
        if(i < j):
            if(arrays[i] @ arrays[j] == 0):
                a = [arrays[i], arrays[j]]
                l.append(a)

print(l)