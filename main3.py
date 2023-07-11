# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными заглавными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def read_string(f):
    s = f.readline()
    if not s:
        f.seek(0)
        s = f.readline()
    return s[:-1]


def f_3(name_num: str, name_name: str, name_result: str):
    with (
        open(name_num, 'r+', encoding='utf-8') as f_num,
        open(name_name, 'r+', encoding='utf-8') as f_name,
        open(name_result, 'w', encoding='utf-8') as f_result
    ):
        len_num = sum(1 for _ in f_num)
        len_name = sum(1 for _ in f_name)

        for i in range(max(len_name, len_num)):
            name = read_string(f_name)
            num = read_string(f_num)
            n1, n2 = map(float, num.split('|'))
            p = n1 * n2
            if p > 0:
                f_result.write(f'{name.upper()} {round(p)} \n' )
            else:
                f_result.write(f'{name.lower()} {abs(p)} \n')


f_3('temp_1.txt', 'temp_2.txt', 'result.txt')

