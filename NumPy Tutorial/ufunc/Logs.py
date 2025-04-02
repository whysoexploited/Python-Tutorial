import numpy as np
from math import log

arr = np.arange(1, 10)
nplog = np.frompyfunc(log, 2, 1)

print(np.log2(arr))
print(np.log10(arr))
print(np.log(arr))
print(nplog(100, 15))