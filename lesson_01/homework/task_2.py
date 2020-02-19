"""
2. Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

WORDS_BYTE = [b"class", b"function", b"method"]


def reveal_type_len(array):
    """функция последоваельно проверяет тип содержимого списка, длину элемента списка и выводит их в консоль"""
    for argument in array:
        print(argument, type(argument), len(argument))


reveal_type_len(WORDS_BYTE)
