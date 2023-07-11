# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции. 

import random

MAX_ = 1000
MIN_ = -1000

def file_nums(file_name, num_str):
    with open(file_name, 'w') as f:
        for _ in range(num_str):
            num1 = random.randint(MIN_, MAX_)
            num2 = random.uniform(MIN_, MAX_)
            stroka = f"{num1}|{num2}\n"
            f.write(stroka)

file_nums("temp_1.txt", 3)