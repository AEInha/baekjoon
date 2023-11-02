from itertools import combinations

a, b= map(int,input().split())
Ls = list(combinations(range(1,a+1), b))
for L in Ls:
  for i in range(len(L)):
    if i == len(L)-1:
      print(L[i])
    else:
      print(L[i],end = ' ')