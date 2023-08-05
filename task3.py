# Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class Baseiscl(Exception):
    pass


class Accesserror(Baseiscl):
    pass


class Levelerror(Baseiscl):
    pass