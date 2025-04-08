# 🧮 Descenso de Gradiente en Polinomios

Este proyecto implementa una simulación visual del descenso de gradiente para encontrar mínimos locales de funciones polinómicas ingresadas por el usuario. Se grafica la función junto con la trayectoria seguida por el algoritmo.
👥 Autor

    David Ricardo Jiménez Núñez


🎯 ¿Qué hace este script?

    Solicita al usuario los coeficientes de un polinomio (por ejemplo: 1 -3 2 para x² - 3x + 2).

    Solicita un rango de evaluación para graficar la función.

    Calcula la derivada simbólicamente a partir de los coeficientes.

    Aplica el descenso de gradiente desde un punto inicial definido por el usuario.

    Visualiza la función, la trayectoria del descenso y el mínimo encontrado.

🧠 Fundamento

El descenso de gradiente es un algoritmo de optimización que busca encontrar el mínimo de una función utilizando su derivada para ajustar la dirección del cambio:

x_new = x - learning_rate * f'(x)

Este script aplica este principio sobre funciones polinómicas reales.
🔧 Requisitos

Asegúrate de tener instaladas las siguientes librerías:

numpy
matplotlib

Puedes instalarlas con:

pip install numpy matplotlib

▶️ Ejecución

    Ejecuta el script en un entorno como Jupyter Notebook, Google Colab o directamente con Python:

python descenso_gradiente.py

    El script solicitará:

    Los coeficientes del polinomio desde el mayor al menor grado.

    El rango de valores a evaluar (ej. -10 10).

    Un punto inicial para iniciar el descenso.

    Se mostrará una gráfica con:

    La curva del polinomio f(x)

    Los pasos que dio el descenso (puntos rojos)

    El mínimo encontrado (punto verde)

🧪 Ejemplo de entrada

Ingresa los coeficientes del polinomio desde el mayor grado al menor (ejemplo: 1, -3, 2): 1 -3 2
Ingresa el rango para evaluar la función (ejemplo: -10 10): -5 5
Ingresa un punto inicial para el descenso de gradiente: 1.5

📊 Visualización generada

    Línea azul: gráfica de la función polinómica.

    Puntos rojos: pasos del descenso de gradiente.

    Punto verde: mínimo local encontrado.

📌 Notas

    El learning_rate está definido por defecto en 0.01, pero puedes modificarlo directamente en el script.

    El algoritmo termina cuando la diferencia entre iteraciones es menor a 1e-6 o se alcanza el máximo de 1000 iteraciones.

📚 Recursos recomendados

    Descenso de Gradiente - Wikipedia

    Numpy - polyval

    Matplotlib - scatter

📝 Licencia

Este proyecto tiene fines educativos y puede usarse libremente.