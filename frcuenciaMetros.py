def frecuencia_a_longitud_onda(frecuencia_hz):
    # Velocidad de la luz en metros por segundo (m/s)
    velocidad_luz = 300000  # m/s
    
    # Longitud de onda (λ) = velocidad de la luz (c) / frecuencia (f)
    longitud_onda_metros = velocidad_luz / frecuencia_hz
    
    return longitud_onda_metros

# Ejemplo de uso:
frecuencia = float(input("Introduce la frecuencia en Hertz: "))
longitud_onda = frecuencia_a_longitud_onda(frecuencia)
print(f"La longitud de onda es: {longitud_onda:.6f} metros")


def longitud_onda_frecuencia(longitud_de_onda):
    # Velocidad de la luz en metros por segundo (m/s)
    velocidad_luz = 300000  # m/s
    
    # Longitud de onda (λ) = velocidad de la luz (c) / frecuencia (f)
    frecuencia_hz = velocidad_luz /longitud_de_onda
    
    return frecuencia_hz


# Ejemplo de uso:
longitudonda = float(input("Introduce la longiud de onda en metros: "))
frecuencia_onda = longitud_onda_frecuencia(longitudonda)
print(f"La frecuencia es: {frecuencia_onda:.6f} Hz")