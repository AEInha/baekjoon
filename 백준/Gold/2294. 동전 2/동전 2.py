import sys

def inp():
  return input()


n,k = map(int,inp().split())
coin = []
for i in range(n):
  coin.append(int(inp()))

coin = list(set(coin))

for i in range(len(coin)):
  if i == 0:
    dp = [i//coin[0] if i%coin[0]==0 else k+1 for i in range(k+1)]
  else:
    for j in range(coin[i],k+1):
      if j == coin[i]:
        dp[j] = min(dp[j],1)
      else:
        if j % coin[i] == 0:
          dp[j] = min(dp[j-coin[i]]+1,j//coin[i],dp[j])
        else:
          dp[j] = min(dp[j-coin[i]]+1,dp[j])

if dp[k] == k+1:
  print(-1)
else:
  print(dp[k])

