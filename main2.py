# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random

glasn = 'AEIOU'
letters = 'AEIOUBCDFGHJKLMNPQRSTVWXYZ'


def gen_names(file_name, num_names):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range (num_names):
            name_len = random.randint(4, 7)
            name_1 = random.choice(glasn)
            for _ in range(name_len - 1):
                name_1 += random.choice(letters)
            stroka = f'{name_1.capitalize()}\n'
            f.write(stroka)

gen_names('temp_2.txt', 10)


