__author__ = 'odmen'

import sys
import gzip

if len(sys.argv) < 2:
        print('''
-l Полный путь до лог-файла
-d Полный путь до дирректории сохранения логов
-z Файл gz
''')
        sys.exit()

gziped = False

for arg in sys.argv:
    # перебираем аргументы, переданные скрипту
    currindex = sys.argv.index(arg)
    # запоминаем индекс текущего выбранного аргумента
    if arg == "-l":
        log_file_path = sys.argv[currindex + 1]
    if arg == "-d":
        log_dir_path = sys.argv[currindex + 1]
    if arg == "-z":
        gziped = True

if gziped:
    curr_logfile = gzip.open(log_file_path, 'rb')
else:
    curr_logfile = open(log_file_path, 'rb')
for line in curr_logfile:
    try:
        line_date = line.decode('utf-8').split(' ')[3][1:]
        line_day = line_date.split('/')[0]
        line_month = line_date.split('/')[1]
        out_file_name = line_day+'-'+line_month
        with gzip.open(log_dir_path+'/'+out_file_name+'.log.gz', 'ab') as curr_out_log:
            curr_out_log.write(line)
    except:
        pass