# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

import sys

ignore = ["duplex", "alias", "configuration"]

if len(sys.argv) == 3:
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        for line in fi:
            if not line.startswith('!'):
                flag_ignore = False
                for i in ignore:
                    if i in line:
                        flag_ignore = True
                        break
                if not flag_ignore:
                    fo.write(line)