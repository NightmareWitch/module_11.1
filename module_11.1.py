import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y)

# Добавление заголовка и подписей осей
plt.title('Пример линейного графика')
plt.xlabel('X ось')
plt.ylabel('Y ось')

# Показ графика
plt.show()