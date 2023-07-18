n,k = map(int,input().split())
dp = [1 for i in range(n)]

if k ==1:
  print(1)
else:
  for j in range(1,k):
    for i in range(n):
      if i == 0:
        dp[i] = (j+1)%1000000000
      else:
        dp[i] = (dp[i-1]+dp[i])%1000000000
  print(dp[n-1]%1000000000)