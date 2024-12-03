import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.linalg import eigvals

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
print(solution.y)

# Graficar la evolución
plt.figure(figsize=(10, 6))
plt.plot(t_eval, S, label='Susceptibles (S)', color='blue')
plt.plot(t_eval, I, label='Infectados (I)', color='red')
plt.plot(t_eval, R, label='Recuperados (R)', color='yellow')
plt.axhline(N, linestyle='--', color='black', label='Población Total (N)')
plt.title("Evolución del modelo SIR modificado")
plt.xlabel("Tiempo (días)")
plt.ylabel("Número de individuos")
plt.legend()
plt.grid()
plt.show()


# Encontrar el tiempo crítico y la fracción de infectados
t_critico_index = np.argmax(I)  # Índice del máximo de infectados
t_critico = t_eval[t_critico_index]  # Tiempo correspondiente
I_max = I[t_critico_index]  # Máximo número de infectados
fraccion_infectados = I_max / N  # Fracción del total de infectados

print(t_critico, I_max, fraccion_infectados)





# Función para calcular el Jacobiano del sistema en un punto dado (S, I, R)
def jacobian(S, I, R):
    # Derivadas parciales con respecto a S, I, R
    df1_dS = -beta * I + mu
    df1_dI = -beta * S
    df1_dR = 0
    
    df2_dS = beta * I
    df2_dI = beta * S - gamma - mu
    df2_dR = 0
    
    df3_dS = 0
    df3_dI = gamma - mu
    df3_dR = -mu
    
    return np.array([[df1_dS, df1_dI, df1_dR],
                     [df2_dS, df2_dI, df2_dR],
                     [df3_dS, df3_dI, df3_dR]])



# Calcular el índice de rigidez a lo largo del tiempo
rigidity_index = []

for S_val, I_val, R_val in zip(S, I, R):
    jac = jacobian(S_val, I_val, R_val)
    # Calcular los autovalores del Jacobiano
    eigvals_jac = eigvals(jac)
    # Tomar el valor absoluto máximo de los autovalores (índice de rigidez)
    rigidity_index.append(np.max(np.abs(eigvals_jac)))

# Graficar el índice de rigidez
plt.figure(figsize=(10, 6))
plt.plot(t_eval, rigidity_index, label="Índice de Rigidez", color='purple')
plt.title("Índice de Rigidez del Sistema SIR Modificado")
plt.xlabel("Tiempo (días)")
plt.ylabel("Índice de Rigidez")
plt.legend()
plt.grid(True)
plt.show()
