import sys

name = sys.stdin.readline()
result = []
flag = 0

for i in range(len(name)):
    if i == 0:
        print(name[i], end='')

    if flag == 1:
        print(name[i], end='')
        flag = 0
        
    if name[i] == '-':
        flag = 1