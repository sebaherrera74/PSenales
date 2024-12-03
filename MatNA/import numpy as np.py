import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parámetros del modelo
N = 1000  # Población total
beta = 0.01  # Tasa de transmisión
mu = 0.3  # Tasa de natalidad/mortalidad
gamma = 1  # Tasa de recuperación

# Condiciones iniciales
S0 = 950  # Susceptibles iniciales
I0 = 50   # Infectados iniciales
R0 = 0    # Recuperados iniciales

# Horizonte de tiempo en días (3 meses)
t_span = (0, 90)  # 3 meses en días
t_eval = np.linspace(t_span[0], t_span[1], 300)  # Tiempo para evaluar

# Sistema de ecuaciones diferenciales
def sir_modified(t, y):
    S, I, R = y
    dS_dt = -beta * S * I + mu * (N - S)
    dI_dt = beta * S * I - gamma * I - mu * I
    dR_dt = gamma * I - mu * R
    return [dS_dt, dI_dt, dR_dt]

# Resolver el sistema
solution = solve_ivp(sir_modified, t_span, [S0, I0, R0], t_eval=t_eval)

# Extraer soluciones
S, I, R = solution.y

# Graficar la evolución
plt.figure(figsize=(10, 6))
plt.plot(t_eval, S, label='Susceptibles (S)', color='blue')
plt.plot(t_eval, I, label='Infectados (I)', color='red')
plt.plot(t_eval, R, label='Recuperados (R)', color='green')
plt.axhline(N, linestyle='--', color='black', label='Población Total (N)')
plt.title("Evolución del modelo SIR modificado")
plt.xlabel("Tiempo (días)")
plt.ylabel("Número de individuos")
plt.legend()
plt.grid()
plt.show()
