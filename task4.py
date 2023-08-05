# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, 
# личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# 📌 Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# 📌 Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует 
# множество пользователей.

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
        
result = json_to_dict('new_user.json')
# print(result)
# print(result[1])
for i in result:
    print(i)
