# Python_Homeworks

## Работа с Allure, Шаги
1. Склонировать проект
2. Установить все зависимости
3. Запустить тесты в ручную или с помощью файла run.sh
4. Сгенерировать отчет из дериктории pytest --alluredir allure-result
5. Открыть результаты отчета allure serve allure-result

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_

### Установка зависимостей
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

### Структура
- ./test - тесты
- ./pages - описание страниц
- ./allure-result - отчетность

### Полезные ссылки
[Подсказка по Мардаун]https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax