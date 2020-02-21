"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet
"""


import subprocess
import chardet


ARGS = {
    'yandex': ['ping', 'yandex.ru'],
    'youtube': ['ping', 'youtube.com'],
}


def ping_resource(args):
    """Функция запускает подпроцесс с аргументами, декодирует ответ выводит
    результаты выполнения в консоль"""
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ping.stdout:
        encoding = chardet.detect(line)
        line = line.decode(encoding['encoding'])
        print(line)


ping_resource(ARGS['yandex'])
ping_resource(ARGS['youtube'])
