# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re

def get_ints_without_description(filename):
    with open(filename) as f:
        # intf = ""
        # for line in f:
        #     line = line.rstrip()
        #     if line.startswith('interface '):
        #         match = re.search(r'interface ([a-zA-Z]\d+(?:/\d+)?(?:\.\d+)?)', line)
        #         if match:
        #             intf = match[1]
        #             descr = ""
        #     elif intf != "" and line.startswith(' description '):
        #         match = re.search(r' description (.+)', line)
        #         if match:
        #             descr = match[1]
        match = re.findall(
                    r'interface ([a-zA-Z]+\d+(?:/\d+)?(?:\.\d+)?)\n'
                    r' (description )?.+\n', f.read())
        return [i for i, d in match if d != 'description ']


if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))
