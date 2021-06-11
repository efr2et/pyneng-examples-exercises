import re

regex = re.compile(r'Host \S+ '
                   r'in vlan (\d+) '
                   r'is flapping between port '
                   r'(\S+) and port (\S+)')

ports = set()

with open('log.txt') as f:
    for m in regex.finditer(f.read()):
        vlan = m.group(1)
        ports.add(m.group(2))
        ports.add(m.group(3))

print('Петля между портами {} в VLAN {}'.format(', '.join(ports), vlan))
