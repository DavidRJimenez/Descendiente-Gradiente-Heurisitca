import numpy as np
import matplotlib.pyplot as plt

# Solicitar coeficientes del usuario
coefficients = list(map(float, input("Ingresa los coeficientes del polinomio desde el mayor grado al menor (ejemplo: 1, -3, 2 para x^2 - 3x + 2): ").strip().split()))
print("Tu función ingresada es: f(x) =", " + ".join([f"{coeff}x^{len(coefficients)-i-1}" for i, coeff in enumerate(coefficients)]))

# Solicitar rango de valores
try:
    range_values = list(map(float, input("Ingresa el rango para evaluar la función (ejemplo: -10 10 para un rango de -10 a 10): ").strip().replace(',', ' ').split()))
    if len(range_values) != 2:
        raise ValueError("Por favor, ingresa dos números para definir el rango.")
    x_values = np.linspace(range_values[0], range_values[1], 500)
except ValueError as e:
    print("Error en el rango ingresado:", e)
    exit()

# Derivada de la función
def derivative_polynomial(x, coefficients):
    derivative_coeffs = [coeff * (len(coefficients) - i - 1) for i, coeff in enumerate(coefficients[:-1])]
    return np.polyval(derivative_coeffs, x)

# Implementación del descenso de gradiente
def gradient_descent(f_coeffs, f_prime, x_init, learning_rate=0.01, tolerance=1e-6, max_iter=1000):
    x = x_init
    history = [x]  # Guardar puntos para visualización
    for _ in range(max_iter):
        grad = f_prime(x, f_coeffs)
        x_new = x - learning_rate * grad
        history.append(x_new)  # Agregar a la trayectoria
        if abs(x_new - x) < tolerance:
            break
        x = x_new
    return x, np.polyval(f_coeffs, x), history

# Solicitar punto inicial
try:
    x_init = float(input("Ingresa un punto inicial para el descenso de gradiente (ejemplo: 0.5): "))
except ValueError as e:
    print("Error en el punto inicial:", e)
    exit()

# Parámetros del descenso de gradiente
learning_rate = 0.01

# Encontrar el mínimo
x_min, f_min, history = gradient_descent(coefficients, derivative_polynomial, x_init, learning_rate)

# Evaluar la función
y_values = np.polyval(coefficients, x_values)

# Graficar la función y la trayectoria del descenso de gradiente
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="f(x)", color="blue")
plt.scatter(history, [np.polyval(coefficients, x) for x in history], color="red", s=10, label="Trayectoria del descenso")
plt.scatter(x_min, f_min, color="green", s=100, label=f"Mínimo encontrado (x = {x_min:.4f}, f(x) = {f_min:.4f})")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.axvline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Visualización del descenso de gradiente")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


