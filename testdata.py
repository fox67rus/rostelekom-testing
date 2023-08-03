import random


def generate_string(n: int) -> str:
    return "x" * n


def generate_russian_string(length):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choice(letters) for i in range(length))


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'  # 20 symbols


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'  # 29 symbols


if __name__ == '__main__':
    pass
