import numpy as np
import time

start = time.time()



rd = np.random.RandomState(88)

for i in range(1,20):
	a = rd.randint(1,1000,(1000,1000))
	y = rd.randint(1,1000,(1000))
	res = np.linalg.solve(a,y)



end = time.time()
print(end-start)