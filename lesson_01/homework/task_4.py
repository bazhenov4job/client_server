"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


WORDS = ['разработка', 'администрирование', 'protocol', 'standard']


def back_and_forth(array):
    """Функция преобразует аргументы в байты, а затем возвращает обратно"""
    for word in array:
        byte_word = word.encode('utf-8')
        word_again = byte_word.decode('utf-8')
        print(
            f'Слово \'{word}\' перевели в байты: {byte_word} и вернули обратно: \'{word_again}\'')


back_and_forth(WORDS)
