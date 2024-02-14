def main(in_file_name: str, out_file_name: str):
    """
    Основная функция.
    Ищет ошибку со значение 55, показывая всю инфу
    :param in_file_name: Название файла для обработки
    :param out_file_name: Название файла для сохранения
    """
    f = open(in_file_name)
    f.readline()
    b = {}
    for line in f.readlines():
        data = line.split('$')
        if '55' in data[2]:
            print(f'У персонажа {data[1]} в игре {data[0]} нашлась ошибка с кодом: {data[2]} Дата фиксации:{data[3]}\n')


if __name__ == '__main__':
    main('game.txt', 'game_new.txt')
