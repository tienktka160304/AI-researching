import numpy as np
from math import log

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))
#1.7005483074552052  = log15(100)