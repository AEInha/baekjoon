import heapq
import sys
N = int(input())
hq = []

for i in range(N):
  n = int(sys.stdin.readline())
  if n== 0:
    if hq:
      a = heapq.heappop(hq)
      print(a)
    else:
      print(0)
  else:
    heapq.heappush(hq,n)