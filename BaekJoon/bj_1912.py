import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0] = num[0]

for i in range(1,n):
    dp[i] = max(num[i], dp[i-1]+num[i])

print(max(dp))