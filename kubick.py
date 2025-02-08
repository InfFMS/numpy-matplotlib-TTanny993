# Задача:
# Смоделируйте 1000 бросков игрального кубика.
# Найдите:
# Сколько раз выпадало каждое значение (от 1 до 6).
# Вероятность выпадения каждого значения.
# Максимальное количество подряд выпавших одинаковых значений.
# Визуализируйте результаты в виде гистограммы.
import numpy as np
import matplotlib.pyplot as plt

t = np.random.randint(1, 7, 1000)
r, values = np.unique(t, return_counts=True)
c = values/10
x = t[0]
cnt = 0
max_cnt = [0] * 6
for el in t:
    if el == x:
        cnt += 1
    else:
        max_cnt[x - 1] = max(max_cnt[x - 1], cnt)
        x = el
        cnt = 1
plt.subplot2grid((2, 2), (0, 0))
plt.bar(r, values, color='red')
plt.xlabel('Результат броска')
plt.ylabel('Количество выпадений')
# plt.show()
plt.subplot2grid((2, 2), (1, 0))
plt.bar(r, c, color='blue')
plt.xlabel('Результат броска')
plt.ylabel('Вероятность выпадения')
# plt.show()
plt.subplot2grid((2, 2), (0, 1), rowspan=2)
plt.bar(r, max_cnt, color='grey')
plt.xlabel('Результат броска')
plt.ylabel('Максимальное количество подряд выпавших одинаковых значений')
plt.tight_layout()
plt.show()