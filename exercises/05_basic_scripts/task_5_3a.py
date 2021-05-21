# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

template_mode = {
    'access': ["interface {}"] + access_template,
    'trunk': ["interface {}"] + trunk_template
}

msg_mode = {
    'access': "Введите номер VLAN: ",
    'trunk': "Введите разрешенные VLANы: "
}
mode = input("Введите режим работы интерфейса (access/trunk): ")
intf = input("Введите тип и номер интерфейса: ")
vlans = input(msg_mode.get(mode,"Неизвестный режим свича, ввод не важен: "))
print("\n".join(template_mode.get(mode, ["Неизвестный режим свича"])).format(intf, vlans))