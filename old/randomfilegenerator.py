import numpy as np

X_1KB = 1024
X_256KB = 256 * X_1KB
X_1MB = 1024 * 1024
X_4MB = 4 * X_1MB
X_32MB = 32 * X_1MB
X_64MB = 2 * X_32MB
X_128MB = X_1MB * 128

#Generate random bytes
out = np.random.bytes( X_1MB )

#Write out to file
f = open('random.bin', 'wb')
f.write(out)
f.close()