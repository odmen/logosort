__author__ = 'odmen'
import string
import random
import os

class StaffFuncs():

    def __init__(self):
        """
        """
        # ---- для id_generator()
        self.size = 6
        # длина последовательности случайных символов
        self.chars = string.ascii_uppercase + string.digits
        # строка из которой будет выбираться случайны символ

        def md5_of_string(self, line):
            d = hashlib.md5()
            d.update(line.encode('utf-8'))
            return d.hexdigest()

        def id_generator(self):
        # функция берет последовательность букв и цифр
        # берет из этой последовательности случайные символы
        # последовательность длинной 6 символов
        # возвращает эту последовательность
            return ''.join(random.choice(self.chars) for _ in range(self.size))

        def create_folder(self, path):
            """
            Функция создает переданную в нее директорию если ее нет.
            Вернет путь до директории в виде строки
            """
            if not os.path.exists(path):
                # print('Каталог '+path+' не существует. Будет создан')
                try:
                    os.makedirs(path)
                    return path
                except Exception as inst:
                    print(type(inst)) # the exception instance
                    print(inst.args) # arguments stored in .args
                    print(inst) # __str__ allows args to printed directly
            # else:
            #     print('Каталог '+path+' существует')