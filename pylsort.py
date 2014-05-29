__author__ = 'odmen'

import os
import sys
import gzip
import argparse
import string
import random

argsparser = argparse.ArgumentParser(description='Сортирует один файл лога по дням')
argsparser.add_argument("-l", required=True, help='Полный путь до файла лога',type=str)
argsparser.add_argument("-d", required=True, help='Каталог для сортированных лог-файлов',type=str)
argsparser.add_argument("-z", required=False, help='Указанный лог файл - .gz', type=int, default=0)
argsparser.add_argument("-v", required=False, help='Выводить сообщения я выполняемых действиях', type=int, default=0)
argumens = argsparser.parse_args()

class LogParser:

    def __init__(self, log_file_path, sorted_logs_path, gzipped):
        self.log_file_path = log_file_path
        self.sorted_logs_path = sorted_logs_path
        self.gzipped = gzipped
        self.parse_log_file()

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create_folder(self):
        interest_folder = self.sorted_logs_path
        if not os.path.exists(interest_folder):
            print('Папка '+interest_folder+' не существует. Будет создана')
            try:
                os.makedirs(interest_folder)
                return interest_folder
            except Exception as inst:
                print(type(inst)) # the exception instance
                print(inst.args) # arguments stored in .args
                print(inst) # __str__ allows args to printed directly
        else:
            print('Папка '+interest_folder+' существует. Файлы будут записаны в эту папку')

    def parse_log_file(self):
        self.create_folder()
        print(self.log_file_path)
        if self.gzipped:
            curr_logfile = gzip.open(self.log_file_path, 'rb')
        else:
            curr_logfile = open(self.log_file_path, 'rb')
        for line in curr_logfile:
            try:
                line = line.decode('utf-8')
                line_date = line.split(' ')[3][1:]
                line_day = line_date.split('/')[0]
                line_month = line_date.split('/')[1]
                out_file_name = line_day+'-'+line_month
                with gzip.open(self.sorted_logs_path+'/'+out_file_name+'.log.gz', 'ab') as curr_out_log:
                    curr_out_log.write(line.encode('utf-8'))
            except Exception as inst:
                print(type(inst)) # the exception instance
                print(inst.args) # arguments stored in .args
                print(inst) # __str__ allows args to printed directly
                print('Current line: '+line)

LogParser(argumens.l,argumens.d,argumens.z)