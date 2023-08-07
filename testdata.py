import random


def generate_string(n: int) -> str:
    return "x" * n


def generate_russian_string(length=10):
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    return ''.join(random.choice(letters) for i in range(length))


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'  # 20 symbols


def special_chars(length=10):
    chars = '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'  # 29 symbols
    return ''.join(random.choice(chars) for i in range(length))


def upper_in_str(text) -> bool:
    if [char for char in text if 65 <= ord(char) <= 90]:
        return True


def lower_in_str(text) -> bool:
    if [char for char in text if 97 <= ord(char) <= 122]:
        return True


def rus_letters_in_str(text) -> bool:
    if [char for char in text if char.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя']:
        return True


def digit_and_spec_in_str(text) -> bool:
    if [char for char in text if char in '0123456789~`!@#$%^&*()_+?:"{}[];’']:
        return True


if __name__ == '__main__':
    pass
