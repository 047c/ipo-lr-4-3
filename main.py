e = int(input(
    "Введите количество чисел, которые хотите упаковать в список: "))  # Получаем количество элементов в
# будущем списке
a = list()  # Создаем новый список для элементов
for i in range(e):
    a.append(
        int(input(f"Введите число, которое хотите поместить на позицию {i} (int): ")))  # Упаковываем числа в список a
print(f"Получившийся список - {a}. Выполняю подсчёт...")  # Выводим получившийся список из while
e = 0  # Обнуляем использованную ранее переменную для нового счётчика
for i in a:  # Подсчитываем количество чисел, больших 10
    if i > 10: # Проверяем больше ли число 10
        e += 1 # Если да, то увеличиваем счётчик на 1
print(f"В списке {e} чисел, больших 10") # Выводим получившийся список
