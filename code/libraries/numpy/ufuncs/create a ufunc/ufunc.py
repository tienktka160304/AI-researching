import numpy as np

def myadd(x, y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
myadd([1,2,3,4],[5,6,7,8])  #[6 8 10 12]
print(type(myadd))
#<class 'numpy.ufunc'>