from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn, 0, method = 'BFGS')

print(mymin)
#   message: Optimization terminated successfully.
#   success: True
#    status: 0
#       fun: 1.75
#         x: [-5.000e-01]
#       nit: 2
#       jac: [ 0.000e+00]
#  hess_inv: [[ 5.000e-01]]
#      nfev: 8
#      njev: 4