__author__ = 'odmen'

import argparse

from logsort import Logsort

argsparser = argparse.ArgumentParser(description=\
    '''
    Сортирует логи. Принимает путь до каталога логов.
    Открывает каждый файл в каталоге, как сжатый, так и нет.
    Ищет в каждом файле строку с датой apache. Парсит дату.
    Создает столько отдельных файлов, сколько есть уникальных
    дат. При этом в каждый файл записывает строку с нужной датой.
    ''')
argsparser.add_help = True
argsparser.add_argument("-d", required=True, help='Полный путь до каталога с логами', type=str)
argsparser.add_argument("-s", required=True, help='Полный путь до каталога с логами', type=str)
argsparser.add_argument("-t", required=False, help='Тип сортировки (D - по дням)', type=str, default="D")
argsparser.add_argument("-v", required=False, help='Выводить сообщения о выполняемых действиях', type=int, default=0)
argus = argsparser.parse_args()

lsort = Logsort()

if argus.t == 'D':
    result = lsort.sort_by_day(argus.d,argus.s)
    for item in result:
        print(item)