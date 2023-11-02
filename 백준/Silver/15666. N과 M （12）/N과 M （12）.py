from itertools import combinations_with_replacement
a, b= map(int,input().split())
k = sorted(list(map(int,input().split())))
Ls = sorted(list(set(list(combinations_with_replacement(k , b)))))
for L in Ls:
  for i in range(len(L)):
    if i == len(L)-1:
      print(L[i])
    else:
      print(L[i],end = ' ')