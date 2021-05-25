# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

result = {}
with open('CAM_table.txt') as f:
    for line in f:
        row = line.rstrip('\n').split()
        if len(row) == 4:
            if row[0].isdigit():
                vlan = int(row[0])
                if vlan in result:
                    result[vlan][row[1]] = row[3]
                else:
                    result[vlan] = {}
                    result[vlan][row[1]] = row[3]

vlan = ""
while not vlan.isdigit():
    vlan = input("Введите номер vlan: ").strip()
    if vlan.isdigit():
        v = int(vlan)
        if 0 < v < 4096:
            if v in result:
                for m in result[v]:
                    print(f"""{v:<9}{m:<20}{result[v][m]}""")
            else:
                print("Этого vlan нет в списке!")
        else:
            print("Не верный номер vlan!")
            vlan = ""
    else:
        print("Не верный номер vlan!")
