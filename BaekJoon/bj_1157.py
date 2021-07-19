import sys
from collections import Counter

word = sys.stdin.readline()
WORD = word.upper()

cnt = Counter(WORD)
count = cnt.most_common()

if(len(WORD)==2):
    print(WORD[0])

else:
    if(count[0][1] == count[1][1]):
        print("?")
    else:
        print(count[0][0])
