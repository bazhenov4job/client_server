"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""


import re
import csv
import chardet


re_prod = re.compile("Изготовитель системы:.+")
re_name = re.compile("Название ОС:.+")
re_code = re.compile("Код продукта:.+")
re_type = re.compile("Тип системы:.+")
re_split = re.compile("\s{2,}")


def detect_encoding(file_name):
    with open(file_name, 'rb') as file:
        line = file.read()
        encoding = chardet.detect(line)
        encoding = encoding['encoding']
    return encoding


def get_data(*files):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file in files:
        encoding = detect_encoding(file)
        with open(file, 'r', encoding=encoding) as info_file:
            text = info_file.read()

            match_prod = re.findall(re_prod, text)
            match_res = re.split(re_split, match_prod[0])
            os_prod_list.append(match_res[1])

            match_name = re.findall(re_name, text)
            match_res = re.split(re_split, match_name[0])
            os_name_list.append(match_res[1])

            match_code = re.findall(re_code, text)
            match_res = re.split(re_split, match_code[0])
            os_code_list.append(match_res[1])

            match_type = re.findall(re_type, text)
            match_res = re.split(re_split, match_type[0])
            os_type_list.append(match_res[1])

    main_data = [['Изготовитель системы',
                  'Название ОС', 'Код продукта', 'Тип системы']]
    spam_list = []
    while len(os_prod_list) > 0:
        spam_list.append(os_prod_list.pop())
        spam_list.append(os_name_list.pop())
        spam_list.append(os_code_list.pop())
        spam_list.append(os_type_list.pop())
        main_data.append(spam_list)
        spam_list = []
    return main_data


def write_to_csv(csv_file):
    with open(csv_file, 'w') as file:
        csv_to_write = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for row in get_data('info_1.txt', 'info_2.txt', 'info_3.txt'):
            csv_to_write.writerow(row)


write_to_csv('data_report.csv')
