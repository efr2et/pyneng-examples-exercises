# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
import sys

ignore = ["duplex", "alias", "configuration"]

if sys.argv[1]:
    with open(sys.argv[1]) as f:
        for line in f:
            if not line.startswith('!'):
                flag_ignore = False
                for i in ignore:
                    if i in line:
                        flag_ignore = True
                        break
                if not flag_ignore:
                    print(line.strip('\n'))
