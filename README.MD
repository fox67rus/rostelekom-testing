Описание
------------
В данном репозитории находится **Итоговый проект по автоматизации тестирования**



Файлы
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base_page.py](pages/base_page.py) contains PageObject pattern implementation for Python.

[pages/auth_page.py](pages/auth_page.py) contains helper class to define web elements on web pages.



Инструкция по запуску
----------------

1) Установить все необходимые библиотеки:

    ```bash
    pip install -r requirements
    ```

2) Скачать Selenium WebDriver по [ссылке](https://chromedriver.chromium.org/downloads) (выбрать версию в соответствии со своим браузером). И положить файл в корневой каталог проекта.

3) Запуск тестов:

    ```bash
    python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/*
    python -m pytest -v -s # вывод доп. информации
    ```
