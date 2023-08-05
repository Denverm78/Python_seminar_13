# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# 📌 Передавайте необходимые данные из основного кода проекта.


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
    try:
        r1, r2 = input('Введите номера двух роботов для сравнения через пробел: ').split(' ')
        try:
            robot1 = result_list[int(r1)-1]
            robot2 = result_list[int(r2)-1]
            break
        except:
            print(f"Как минимум одно из чисел '{r1}' и '{r2}' введено некорректно")
    except:
        print('Что-то пошло не так, давайте еще раз')
    
        
    
if robot1.model > robot2.model:
    print(robot1.name)
else:
    print(robot2.name)