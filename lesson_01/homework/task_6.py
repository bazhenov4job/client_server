"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но отерыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""


from chardet.universaldetector import UniversalDetector


WORDS = ["сетевое программирование", "сокет", "декоратор"]
NEW_FILE = open('test_file.txt', 'w')
NEW_FILE.write('\n'.join(WORDS))
NEW_FILE.close()
DETECTOR = UniversalDetector()

# Проверяем кодировку файла по умолчанию
with open('test_file.txt', 'rb') as test_file:
    for line in test_file:
        DETECTOR.feed(line)
        if DETECTOR.done:
            break
    DETECTOR.close()
    ENCODING = DETECTOR.result['encoding']
print(ENCODING)

# Откроем файл в кодировке UTF-8
# Хотел применить к этому всему сэндвич, но не придумал как. Попытка line.encode('utf-8') не удаётся,
# видимо объетк заведомо не удаётся обработать и возбуждается исключение

with open('test_file.txt', encoding='UTF-8') as test_file:
    try:
        for line in test_file:
            print(line)
    except UnicodeDecodeError:
        NEW_TEST = open('test_file.txt', encoding=ENCODING)
        for line in NEW_TEST:
            print(line)
        NEW_TEST.close()
