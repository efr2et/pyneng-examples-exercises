# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

correct_ip = False
while not correct_ip:
    ip = input("Введите ip: ")
    ip.strip()
    ipo = ip.split(".")
    if ip.count(".") != 3:
        print("Неправильный IP-адрес")
    elif len(ipo) != 4:
        print("Неправильный IP-адрес")
    else:
        for i in ipo:
            if not i.isdigit():
                print("Неправильный IP-адрес")
                break
            elif not 0 <= int(i) <= 255:
                print("Неправильный IP-адрес")
                break
        else:
            correct_ip = True
            if 0 < int(ipo[0]) < 224:
                print("unicast")
            elif 223 < int(ipo[0]) < 240:
                print("multicast")
            elif ip == "255.255.255.255":
                print("local broadcast")
            elif ip == "0.0.0.0":
                print("unassigned")
            else:
                print("unused")
