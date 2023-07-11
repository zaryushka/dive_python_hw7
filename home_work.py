# Домашнее задание


# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


import os

def rename_group_files(new_name, numerate_num, orig_ext, new_ext, range_name):
    dir = os.getcwd()
    print(f'dir = {dir}')

    # список всех файлов в директории
    files_list_all = os.listdir(dir)
    # фильтруем по нужному расширению
    files_filter_ext = [file for file in files_list_all if file.endswith(orig_ext)]
    print(files_filter_ext)

    # получаем путь к текущим файлам
    for i, file in enumerate(files_filter_ext):
        file_path_old = os.path.join(dir, file)

    # обрезаем имя по нужному диапазону
        new_file_name = file[range_name[0] - 1:range_name[1]]
        print(new_file_name)

    # собираем имя файла
        new_file_name = new_file_name + new_name + str(i).zfill(numerate_num) + new_ext
        print(new_file_name)

    # получаем путь к файлам с новым именем
        file_path_new = os.path.join(dir, new_file_name)

        os.rename(file_path_old, file_path_new)

rename_group_files('summer_file', 2, '.png', '.jpg', [2, 4])


