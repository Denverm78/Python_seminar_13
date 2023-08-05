# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# 📌 загрузка данных (функция из задания 4)
# 📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
# в множестве используйте магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, 
# получите его уровень из множества пользователей.
# 📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, 
# вызывайте исключение уровня доступа.

import json

class Robot():
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def __str__(self) -> str:
        return (f'Robot - {self.name}, модель - {self.model}')


def json_to_dict(file_name):
    robot_list = []
    with open(file_name, 'r', encoding='utf-8') as f_json:
        dict_robots = json.load(f_json)
    for key in dict_robots:
        robot = Robot(key, dict_robots[key])
        robot_list.append(robot)
    return robot_list
        
result_list = json_to_dict('new_user.json')

while True:
    r1, r2 = input('Введите номера двух роботов для сравнения через пробел: ').split(' ')
    try:
        robot1 = result_list[int(r1)-1]
        robot2 = result_list[int(r2)-1]
        break
    except:
        print("Как минимум одно из чисел введено некорректно")
        
    
if robot1.model > robot2.model:
    print(robot1.name)
else:
    print(robot2.name)