"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""


import yaml


FIRST_KEY = ['some', 'list', 'spam']

SECOND_KEY = 123

THIRD_KEY = {'spam': {'eggs': '\u0210', 'monty': '\u0211'}}

MAIN_DICT = {'first': FIRST_KEY,
             'second': SECOND_KEY,
             'third': THIRD_KEY
             }

with open('test_file.yaml', 'w', encoding='UTF-8') as yaml_file:
    yaml.dump(
        MAIN_DICT,
        yaml_file,
        default_flow_style=False,
        allow_unicode=True)


# И это кстати очень интересный момент - я про Loader, потому что с BaseLoader число int он
# загружал мне, как строку
with open('test_file.yaml', 'r', encoding='utf-8') as yaml_file:
    DATA = yaml.load(yaml_file, Loader=yaml.FullLoader)

if MAIN_DICT == DATA:
    print(True)
else:
    print(False)
