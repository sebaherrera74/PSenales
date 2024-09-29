import numpy as np
import pandas as pd

# Define the function and its derivative
def f(x):
    return x**2 - 2

def df(x):
    return 2*x

# Define Bisection method
def bisection(a, b, tol, max_iter):
    iterations = []
    for n in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        if abs(f(c)) < tol or abs(b - a) / 2 < tol:
            break
        if f(c) * f(a) > 0:
            a = c
        else:
            b = c
    return iterations

# Define Newton's method
def newton(x0, tol, max_iter):
    iterations = [x0]
    for n in range(max_iter):
        x1 = x0 - f(x0) / df(x0)
        iterations.append(x1)
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return iterations

# Define Secant method
def secant(x0, x1, tol, max_iter):
    iterations = [x0, x1]
    for n in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append(x2)
        if abs(x2 - x1) < tol:
            break
        x0, x1 = x1, x2
    return iterations

# Set tolerance and maximum iterations
tol = 1e-6
max_iter = 100

# Run each method
bisection_iterations = bisection(1, 2, tol, max_iter)
newton_iterations = newton(1, tol, max_iter)
secant_iterations = secant(0.5, 1, tol, max_iter)
#print(bisection_iterations)

# Create table of results
results = pd.DataFrame({
    'Bisection': bisection_iterations,
    'Newton': newton_iterations + [None]*(len(bisection_iterations) - len(newton_iterations)),
    'Secant': secant_iterations + [None]*(len(bisection_iterations) - len(secant_iterations))
})

print(results)
"""
# Estimate order of convergence
def estimate_convergence(iterations):
    p = []
    for i in range(2, len(iterations)):
        p_i = np.log(abs(iterations[i] - np.sqrt(2)) / abs(iterations[i-1] - np.sqrt(2))) / \
              np.log(abs(iterations[i-1] - np.sqrt(2)) / abs(iterations[i-2] - np.sqrt(2)))
        p.append(p_i)
    return p

bisection_order = estimate_convergence(bisection_iterations)
newton_order = estimate_convergence(newton_iterations)
secant_order = estimate_convergence(secant_iterations)

# Add orders of convergence to the table
orders = pd.DataFrame({
    'Bisection Order': [None, None] + bisection_order,
    'Newton Order': [None, None] + newton_order + [None]*(len(bisection_order) - len(newton_order)),
    'Secant Order': [None, None] + secant_order + [None]*(len(bisection_order) - len(secant_order))
})

# Combine results and orders
combined_results = pd.concat([results, orders], axis=1)
combined_results
"""