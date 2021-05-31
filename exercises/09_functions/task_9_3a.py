# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        intf = ""
        access_dict = {}
        trunk_dict = {}
        for line in f:
            if "interface " in line:
                intf = line.split()[1]
            elif "trunk allowed vlan" in line:
                trunk_dict[intf] = [
                    int(vlan) for vlan in
                    line.replace("switchport trunk allowed vlan", "").replace(" ", "").strip('\n').split(',')
                ]
            elif "switchport access vlan" in line:
                access_dict[intf] = int(line.split()[-1])
            elif "switchport mode access" in line:
                if intf not in access_dict:
                    access_dict[intf] = 1
    return access_dict, trunk_dict


print(get_int_vlan_map("config_sw2.txt"))

