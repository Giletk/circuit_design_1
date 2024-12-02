import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Чтение данных из файла
with open(r"C:\Learning\ЭлТех\CircuitDesign_lab_0\source\input2.txt", "r") as f:
    lines = f.readlines()
lines = [[float(x) for x in line.split()] for line in lines]

# Извлечение данных
t = np.array([line[1] for line in lines])
u1 = np.array([line[2] for line in lines])
u2 = np.array([line[3] for line in lines])

# Линейизация данных
ln_u1 = np.log(u1)  # Логарифм значений

# Линейная аппроксимация (MНК для линейной формы)
coefficients = np.polyfit(t, ln_u1, deg=1)
ln_u1_approx = np.polyval(coefficients, t)  # Линейная аппроксимация
u1_approx = np.exp(ln_u1_approx)  # Обратное преобразование

# Построение графиков
# plt.scatter(t, u1, color='r', label="Практика")  # Исходные данные
plt.plot(t, u1_approx, color='b', label="Приактика")  # Линейная аппроксимация
plt.plot(t, u2, color='g', label="Теория")
plt.xlabel("t, с")
plt.ylabel("U, В")
plt.legend()
# plt.title("Аппроксимация экспоненциальной зависимости через ленеаризацию")
plt.grid()
plt.show()

# Вывод коэффициентов
E0 = np.exp(coefficients[1])  # exp(ln(E0))
tau = -1 / coefficients[0]  # -1 / коэффициент наклона
print(f"E_0 = {E0}, tau = {tau}")
