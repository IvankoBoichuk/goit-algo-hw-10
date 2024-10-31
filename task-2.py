import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# 1. Обчислення інтеграла функції методом Монте-Карло
# Вибираємо кількість точок
num_points = 100000

# Генеруємо випадкові точки в межах інтеграції
x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, f(b), num_points)

# Обчислюємо кількість точок під кривою
under_curve = y_random < f(x_random)
monte_carlo_area = (b - a) * f(b) * np.sum(under_curve) / num_points

# 2. Перевірка правильності розрахунків за допомогою функції quad
analytical_result, error = quad(f, a, b)

# Графік функції та метод Монте-Карло
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3, label='Площа під кривою')

# Точки для Монте-Карло
ax.scatter(x_random, y_random, color='blue', s=0.5, alpha=0.1, label='Точки Монте-Карло')
ax.scatter(x_random[under_curve], y_random[under_curve], color='green', s=0.5, alpha=0.1, label='Під кривою')

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для інтеграції f(x) = x^2 від {} до {}'.format(a, b))
ax.legend()
plt.grid()
plt.show()

print(monte_carlo_area, analytical_result, error)