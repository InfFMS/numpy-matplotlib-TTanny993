# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import numpy as np
import matplotlib.pyplot as plt

t = np.random.randint(-10, 36, 365)
mean_t = t.mean()
high_t = len(t[t > 25])
max_row=0
cnt=0
for tmp in t:
    if tmp < 0:
        cnt += 1
    else:
        max_row = max(max_row, cnt)
        cnt = 0
print(mean_t, high_t, max_row, sep='\n')

amount_days = np.arange(1, 366)
plt.subplot2grid((1, 2), (0, 0))
plt.plot(amount_days, t, color='black')
plt.xlabel('День')
plt.ylabel('Температура')
x = np.array([])
y = np.array([])
colors = np.array([])
for i in range(365):
    s = False
    if t[i] > 25:
        color = 'red'
        s = True
    elif t[i] < 0:
        color = 'blue'
        s = True
    if s:
        x = np.append(x, i)
        y = np.append(y, t[i])
        colors = np.append(colors, color)
plt.scatter(x, y, color=colors)
unique_t, cnt_days = np.unique(t, return_counts=True)
plt.subplot2grid((1, 2), (0, 1))
plt.bar(unique_t, cnt_days, color='blue')
plt.xlabel('Температура')
plt.ylabel('Количество дней')
plt.tight_layout()
plt.show()