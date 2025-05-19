# constante da gravidade
g = 9.81 # m/s²

# entrada de dados
v0 = float(input("digite a velocidade inicial (m/s²): "))
t = float(input("digite o tempo (s): "))

# cálculos 
# altura máxima (quando a velocidade final é 0)
h_max = ((v0 ** 2) / (2 * g))

# tempo até a altura máxima
t_subida = (v0 / g)

# posição no tempo t
# s = v0 * t - (1/2) *g * t²
h_t = (v0 * t - 0.5 * g * (t ** 2))


# saída 
print(f"/altura máxima: {h_max:.2f}m")
print(f"tempo de subida: {t_subida:.2f}s")
print(f"altura no instante t={t:.2f}s: {h_t:.4f}m") 