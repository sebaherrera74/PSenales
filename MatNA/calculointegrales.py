#Calculo de Integrales
from sympy import symbols, integrate, exp, oo

# Definir la variable simbólica
x = symbols('x')

# Definir las funciones a integrar
f0= x * exp(-2*x)  # Integral de x^2 * e^(-2x)
f1 = x**2 * exp(-2*x)  # Integral de x^2 * e^(-2x)
f2 = x**3 * exp(-2*x)  # Integral de x^3 * e^(-2x)
f3 = x**4 * exp(-2*x)  # Integral de x^4 * e^(-2x)

# Calcular las integrales definidas
integral_f0_def = integrate(f0, (x, 5, 0))  # De 0 a infinito
integral_f1_def = integrate(f1, (x, 5, 0))  # De 0 a infinito
integral_f2_def = integrate(f2, (x, 5, 0))  # De 0 a infinito
integral_f3_def = integrate(f3, (x, 5, 0))  # De 0 a infinito

# Mostrar resultados
print("Integral definida de x * e^(-2x) de 0 a infinito:", float(integral_f0_def))
print("Integral definida de x^2 * e^(-2x) de 0 a infinito:", float(integral_f1_def))
print("Integral definida de x^3 * e^(-2x) de 0 a infinito:", float(integral_f2_def))
print("Integral definida de x^4 * e^(-2x) de 0 a infinito:", float(integral_f3_def))
