import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')

# Configurar el generador de números aleatorios
rng = np.random.RandomState(0)

# Generar un rango de valor en el eje x
x = np.linspace(0, 10, 500)

# Generar datos aleatorios y calcular la suma acumulativa
y = np.cumsum(rng.randn(500, 6), axis=0)

# Graficar los datos
sns.set()
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

y_val = x ** 2
plt.scatter(x, y_val, marker='s', color='g')
plt.title('Gráfico de dispersión')
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()
