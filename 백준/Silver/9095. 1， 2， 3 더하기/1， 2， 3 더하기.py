T=int(input())




def jump(N,K):
  if K + 3 <=N:
    return jump(N,K+3) + jump(N,K+2) + jump(N,K+1) 
  elif K +2 <=N:
    return jump(N,K+2) + jump(N,K+1) 
  elif K +1 <=N:
    return jump(N,K+1) 
  else:
    return 1

for i in range(T):
  K = 0
  N = int(input())
  print(jump(N,K))