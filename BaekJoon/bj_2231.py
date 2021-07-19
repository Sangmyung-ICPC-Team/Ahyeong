import sys

n = int(sys.stdin.readline()) 

for i in range(1,n+1): 
    arr = list(map(int, str(i))) 

    if sum(arr) + i == n: 
        print(i) 
        exit()

print(0)
