import numpy as np
from numpy import random
import time

start = time.time()

for i in range(1,20):
	np.random.rand(10**5)

end = time.time()
print(end-start)



