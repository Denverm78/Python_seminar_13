# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, 
# пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.

def get_number():

    while True:
        num = input('Введите целое или вещественное число: ')
        try:
            num = float(num)
            return num
        except:
            print('Вы ввели не число!')


print(get_number())