from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myroot = root(eqn, 0)

print(myroot)
#  message: The solution converged.
#  success: True
#   status: 1
#      fun: [ 0.000e+00]
#        x: [-7.391e-01]
#   method: hybr
#     nfev: 9
#     fjac: [[-1.000e+00]]
#        r: [-1.674e+00]
#      qtf: [-2.668e-13]