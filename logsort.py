__author__ = 'odmen'

import os
import gzip
import re

from logstaff import StaffFuncs

class Logsort():

    def __init__(self):
        """
        Класс создан для сортировки логов по заданному критерию.
        1. Сортирует логи по дням. Принимает на вход каталог с логами.
        Считает что все файлы в этом каталоге - текстовые файлы с логами.
        """
        self.staffunc = StaffFuncs()
        self.datereg = re.compile(b'\[[0-9]{2}\/[A-Z][a-z]{2}\/[0-9]{4}:(([0-9]){2}:){2}[0-9]{2}\s\+[0-9]{4}\]')
        # регулярка даты в фомате [01/Jan/2014:00:00:00 +0400]
        self.created_files = set() # список созданных файлов

    def __exit__(self):
        self.created_files.clear()

    def sort_by_day(self, fpath, tpath):
        """
        Сортирует все файлы в указаном каталоге по дням
        День выбирает по дате. Предполагается, что в каждой строке
        содержится дата в формате [01/Jan/2014:00:00:00 +0400]
        """
        if not os.path.exists(fpath):
            print("Folder "+fpath+" does not exist")
            return
        else:
            if not os.path.exists(tpath):
                self.staffunc.create_folder(tpath)
            logfiles = os.listdir(fpath)
            for lfile in logfiles:
                lfilepath = fpath+'/'+lfile
                try:
                    if lfilepath[-2:] == 'gz':
                        # Если имя файла заканчивается на "gz"
                        # то пробуем открыть файл как не сжатый
                        curlogfile = gzip.open(lfilepath, 'rb').readlines()
                    else:
                        # если имя файла заканчивается на не "gz"
                        # то пробуем открыть файл как не сжатый текст
                        curlogfile = open(lfilepath, 'rb').readlines()
                except Exception as excinfo:
                    print("Exception in sort_by_day(): open('"+lfilepath+"', 'rb') "+str(excinfo))
                try:
                    for line in curlogfile:
                        if self.datereg.search(line):
                            # если в текущей строке найдена
                            # дата в подходящем формате
                            curlinedate = self.datereg.search(line).group().decode('utf-8')
                            # тут только дата из текущей строки. Вида
                            # "[01/Jan/2014:00:00:00 +0400]"
                            curlinedate = '-'.join(curlinedate.strip('[]').split('/')[:2])
                            # тут число и день этой даты в виде "01-Jan"
                            if os.path.exists(tpath):
                                curwln = tpath+"/"+curlinedate+".log"
                                # полный путь для текущего сохраняемого файла:
                                # /tmp/psth0/path1/01-Jan.log
                                try:
                                    with open(curwln, 'ab+') as curfw:
                                        curfw.write(line) # пишем строку в файл
                                except Exception as excinfo:
                                    print("Exception in sort_by_day(): writing lines to '"+curwln+"': "+str(excinfo))
                                self.created_files.add(curwln)
                                # добавляем имя файла в список созданных файлов
                except Exception as excinfo:
                    print("Exception in sort_by_day(): reading lines from '"+lfilepath+"': "+str(excinfo))
            return self.created_files
            # Возвращаем список путей сохраненных файлов