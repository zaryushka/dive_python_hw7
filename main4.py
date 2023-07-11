# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import os
import random


leters = 'AEIOUBCDFGHJKLMNPQRSTVWXYZ'

def create_files(ext, min_name=6, max_name=30, min_bytes=256, max_bytes=4096, files=5):
    for i in range(files):
        # Генерируем случайное имя файла
        name_len = random.randint(min_name, max_name)
        file_name = ''.join(random.choices(leters, k=name_len)) + ext

        # Генерируем случайное количество байт
        num_bytes = random.randint(min_bytes, max_bytes)
        data = os.urandom(num_bytes)

        # Записываем данные в файл
        with open(file_name, 'wb') as file:
            file.write(data)

        print(f'файл - {file_name} размер {num_bytes} байт')


create_files('.png')
