# Проект парсера PEP с использованием Scrapy

![Логотип проекта](logo.png)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Scrapy ](https://img.shields.io/badge/-Scrapy-464646?style=flat&logo=Scrapy&logoColor=ffffff&color=043A6B)](https://github.com/scrapy/scrapy)
[![Coverage](./htmlcov/index.html)](./htmlcov/index.html)

Этот проект представляет собой парсер `PEP (Python Enhancement Proposals)` с использованием фреймворка `Scrapy`. Основной задачей парсера является сохранение всех названий существующих `PEP` в файле и подсчет документов в соответстии статусу.

## Функциональность и особенности

- Парсинг `PEP`: Парсер использует `Scrapy` для извлечения данных о `PEP` с официального сайта `Python`.
- Сохранение данных: Все названия, номера и статусы `PEP` сохраняются в файле `pep_ДатаВремя.csv`.
- Подсчет статусов: Парсер подсчитывает количество `PEP` в каждом из следующих статусов: `Draft`, `Active`, `Final`, `Rejected` и др.
- Результат так же сохраняется в отдельном файле `status_summary_ДатаВремя.csv`.

## Зависимости

- `Python 3.8.10`
- `Scrapy`

## Установка и использование

1. Установите `Python 3.8.10`, если его еще нет.
2. Склонируйте репозиторий проекта:

```python
   git clone git@github.com:Pankirbor/scrapy_parser_pep.git
```
3. Создайте и активируйте виртуальное окружение:

```python
    python3 venv venv
    source venv/bin/activate
```
4. Установите все зависимомти из файла `requirements.txt` с помощью следующей команды:

```python
   pip install -r requirements.txt
```
5. Перейдите в директорию проекта:

```python
   cd  scrapy_parser_pep
```
6. Запустите парсер с помощью команды:

```python
   scrapy crawl pep
```

   Эта команда запустит парсер и сохранит результаты в двух файлах `pep_ДатаВремя.csv` и `status_summary_ДатаВремя.csv`.


## Фрагменты получаемых таблиц
| number                 | name                              | status
|------------------------|-----------------------------------|------------------------------|
|250|Using site-packages on Windows|Final
|254|Making Classes Look More Like Types|Rejected
|255|Simple Generators|Final|

| Статус  | Количество|
|---------|-----------|
| Final   | 276       |
| Rejected| 122       |
| Active  | 31        |


## Вклад и участие

Если вы хотите внести свой вклад в проект, вы можете сделать следующее:
- Форкните репозиторий проекта на `GitHub`.
- Создайте новую ветку для ваших изменений: `git checkout -b feature/your-feature`.
- Внесите необходимые изменения и коммиты.
- Отправьте свои изменения в форкнутый репозиторий: `git push origin feature/your-feature`.
- Создайте `Pull Request`, описывающий ваши изменения и предлагающий их для включения в основной репозиторий.



## Дополнительные ресурсы

- [Документация Scrapy](https://docs.scrapy.org/)
- [PEP](https://peps.python.org/)

### Разработчик
[Кирилл Панов](https://github.com/Pankirbor)
