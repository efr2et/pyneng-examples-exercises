# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

import subprocess as sp
from pprint import pprint

ips = [
    '1.1.1.1',
    '8.8.8.8',
    '127.1.1.1',
    '192.168.1.1'
]

def ping_ip_addresses(ip_list):
    ok = []
    nok = []

    for l in ip_list:
        r = sp.run(['ping', '-c 1', '-q', l], stdout=sp.PIPE, stderr=sp.PIPE)
        if r.returncode == 0:
            ok += [l]
        else:
            nok += [l]

    return ok, nok


if __name__ == '__main__':
    pprint(ping_ip_addresses(ips))
