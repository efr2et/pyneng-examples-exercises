# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate
from task_12_1 import ping_ip_addresses
from task_12_2 import convert_ranges_to_ip_list

ips = [
    '1.1.1.1',
    '8.8.8.8',
    '127.1.1.1',
    '192.168.1.1'
]


def print_ip_table(reach, unreach):
    print(tabulate({'Reachable': reach, 'Unreachable': unreach}, headers='keys'))
    return


if __name__ == '__main__':
    print_ip_table(*ping_ip_addresses(convert_ranges_to_ip_list(ips)))

