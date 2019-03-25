import numpy as np

ncodes = 4



black = np.empty((ncodes, ncodes))

for i in range(ncodes):
    for j in range(i+1):
        print(i,j, str(i)+str(j), i+10*j, np.random.randint(10))
        
        b = np.random.randint(10)
        black[i,j] = b
        black[j,i] = b
        
        
print(black)        
        