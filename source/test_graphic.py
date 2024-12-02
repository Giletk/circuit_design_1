import numpy as np
import matplotlib.pyplot as plt

def least_squares_fit(x, y):
    # Преобразование списков в массивы numpy
    x = np.array(x)
    y = np.array(y)
    
    # Расчет коэффициентов линейной регрессии
    A = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    
    return m, c

def plot_least_squares(x, y, m, c):
    # Построение графика исходных данных
    plt.scatter(x, y, label='Исходные данные')
    
    # Построение линии линейной регрессии
    plt.plot(x, m*x + c, 'r', label='Линейная регрессия')
    
    # Добавление подписей к осям и легенды
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    
    # Отображение графика
    plt.show()

# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 4, 6]

# Расчет коэффициентов линейной регрессии
m, c = least_squares_fit(x, y)

# Построение графика
plot_least_squares(x, y, m, c)
