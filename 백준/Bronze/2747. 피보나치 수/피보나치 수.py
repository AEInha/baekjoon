n = int(input())
dp = [0 for i in range(n+1)]
dp[0] = 0
dp[1] = 1
if n == 0:
  print(dp[0])
elif n == 1:
  print(dp[1])
else:
  for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

  print(dp[n])