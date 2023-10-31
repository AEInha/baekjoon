import sys
S = set()

def inp():
  return sys.stdin.readline()

M = int(inp())
for i in range(M):
  a = inp()
  L = a.split()
  if L[0] == 'add':
    S.add(int(L[1]))
  elif L[0] == 'remove':
    S.discard(int(L[1]))
  elif L[0] == 'check':
    if int(L[1]) in S:
      print(1)
    else:
      print(0)
  elif L[0] == 'toggle':
    if int(L[1]) in S:
      S.discard(int(L[1]))
    else:
      S.add(int(L[1]))
  elif L[0] =='all':
    S = set([i for i in range(1,21)])
  else:
    S = set()