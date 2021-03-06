# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

net = input("Введите IP-сети в формате X.X.X.X/X: ")
ip, mask = net.split("/")
ipo = ip.split(".")
maskb = "1" * int(mask) + "0" * (32 - int(mask))

print(f"""Network:
{ipo[0]:10}{ipo[1]:10}{ipo[2]:10}{ipo[3]:10}
{bin(int(ipo[0]))[2:]:0>8}  {bin(int(ipo[1]))[2:]:0>8}  {bin(int(ipo[2]))[2:]:0>8}  {bin(int(ipo[3]))[2:]:0>8}

Mask:
/{mask}
{int(maskb[0:8],2):<10}{int(maskb[8:16],2):<10}{int(maskb[16:24],2):<10}{int(maskb[24:32],2):<10}
{maskb[0:8]:8}  {maskb[8:16]:8}  {maskb[16:24]:8}  {maskb[24:32]:8}
""")