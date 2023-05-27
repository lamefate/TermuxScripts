def list_aliases():
    aliases=[]
    with open('/data/data/com.termux/files/usr/etc/bash.bashrc', 'r') as bashrc:
        for line in bashrc.readlines():
            if 'alias' in line:
                if not 'list_aliases.py' in line:
                    line = line.replace('alias ', '')
                    aliases.append(line)
        bashrc.close()
    print('aliases:')
    for alias in aliases:
        alias = alias.split('=')
        print('\t{} -> {}'.format(alias[0], alias[1]), end="")

list_aliases()
