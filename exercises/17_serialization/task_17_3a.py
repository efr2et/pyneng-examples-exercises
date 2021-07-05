# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод
команды show cdp neighbor из нескольких файлов и записывает итоговую
топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами,
независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь
в файл topology.yaml. Он понадобится в следующем задании.

"""
import glob
import re
import yaml
from pprint import pprint

sh_cdp_files = glob.glob("sh_cdp*.txt")


def parse_sh_cdp_neighbors(output):
    result = {}
    match = re.search(r'([a-z0-9._-]+)\s*>', output, re.S | re.M | re.I)
    if match:
        dev = match[1]
        regex = re.compile(r'([a-z0-9._-]+)\s+'
                           r'([a-z0-9]+ [0-9]+/*(?<=/)[0-9]*)\s+'
                           r'\d+\s*'
                           r'[RTBSHIrP ]*'
                           r'[a-z0-9._-]+\s*'
                           r'([a-z0-9]+ [0-9]+/*(?<=/)[0-9]*)\s*', re.S | re.M | re.I)
        result[dev] = {m[2]: {m[1]: m[3]} for m in regex.finditer(output)}
    return result


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    pprint(list_of_files)
    result = {key: value for list_dict in [parse_sh_cdp_neighbors(open(fn).read())
                                           for fn in list_of_files]
              for key, value in list_dict.items()}
    if save_to_filename:
        with open(save_to_filename, 'w') as f:
            if result:
                yaml.dump(result, f, default_flow_style=False)
    return result


if __name__ == '__main__':
    pprint(generate_topology_from_cdp(sh_cdp_files, 'sh_cdp_files.yaml'))
