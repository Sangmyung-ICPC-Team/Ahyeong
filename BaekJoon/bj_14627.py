import sys

S, C = map(int, sys.stdin.readline().split())
s = []

for _ in range(S):
    s.append(int(sys.stdin.readline()))

start = 0
end = max(s)

while start <= end:
    mid = (start + end) // 2

    if mid == 0:
        mid = 1
        
    cnt = 0
    for i in s:
        cnt += i//mid

    if(cnt >= C):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

sum = 0
for i in s:
    sum += i
    
print(sum - result*C)