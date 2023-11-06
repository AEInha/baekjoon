from itertools import combinations
import sys
from collections import deque
input = sys.stdin.readline
def make_dslr(n):
  D = (2*n)%10000
  S = n-1
  if n == 0:
    S = 9999
  d1,d2,d3,d4 = n//1000,(n%1000)//100,((n%1000)%100)//10,((n%1000)%100)%10
  L = ((d2 * 10 + d3) * 10 + d4) * 10 + d1
  R = ((d4 * 10 + d1) * 10 + d2) * 10 + d3
  return [D,S,L,R]


def bfs(start,target_num):
  visited = set()
  will_visited = deque()
  will_visited.append(start)
  parenta = {}
  parenta[start] = ' '
  while True:
    location = will_visited.popleft()
    if location == target_num:
      break
    else:
      if location in visited:
        continue
      else:
        visited.add(location)
        Ls = make_dslr(location)
        k = 0
        A = ['D','S','L','R']
        for L in Ls:
          if L not in parenta.keys():
            if A[k] =='L':
              if parenta[location][-1] == 'R':
                continue
              elif parenta[location][-2:] == 'LL':
                continue
              else:
                parenta[L] = parenta[location] + A[k]
                will_visited.append(L)
            elif A[k] == 'R':
              if parenta[location][-1] == 'L':
                continue
              else:
                parenta[L] = parenta[location] + A[k]
                will_visited.append(L)
            else:
              parenta[L] = parenta[location] + A[k]
              will_visited.append(L)

          k+=1
  return parenta[location].strip()







T = int(input())
for i in range(T):
  start,target_num = map(int,input().split())
  print(bfs(start,target_num))