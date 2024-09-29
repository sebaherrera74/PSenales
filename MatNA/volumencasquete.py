import math

# Definir la función para calcular el volumen del casquete esférico
def volumen_casquete(R, h):
    return (math.pi * h**2 * (3 * R - h)) / 3

# Valores de ejemplo
R = 1  # radio de la esfera
h = 1  # altura del líquido

# Calcular el volumen
volumen = volumen_casquete(R, h)
print(f"El volumen del casquete esférico es: {volumen:.2f}")