import random
from faker import Faker


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
    locale_list = ['en-US', 'ja-JP', 'zh_CN', 'ru_RU']
    fake = Faker(locale_list)

    for _ in range(3):
        print(fake['ru_RU'].name())
        print(fake['ja_JP'].sentence(nb_words=5))

    for _ in range(3):
        print(fake['ru_RU'].sentence())

    # names = [fake_ru.unique.first_name() for i in range(5)]
    # print(names)

    for _ in range(3):
        print(fake.emoji())

    for _ in range(5):
        print(fake.lexify(text='??????????'))

