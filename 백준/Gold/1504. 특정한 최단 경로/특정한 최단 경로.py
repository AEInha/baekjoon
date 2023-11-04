from itertools import permutations
from itertools import permutations
import heapq
import sys
INF = sys.maxsize
N,E = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}

for i in range(E):
  u,v,w= map(int,input().split())
  graph[u].append([v,w])
  graph[v].append([u,w])







def dji(start,graphs):
  distance = [INF]*(len(graphs)+1)
  hp = []
  heapq.heappush(hp,(0,start))
  distance[start] = 0
  while hp:
    w,v = heapq.heappop(hp)
    if distance[v] < w:
      continue
    else:
      for graph in graphs[v]:
        v_2,w_2 = graph[0],graph[1]
        cost = w_2 + distance[v]
        if distance[v_2] > cost:
          distance[v_2] = cost
          heapq.heappush(hp,(cost,v_2))

  return distance

V_1,V_2 = map(int,input().split())


L = {1:[],V_1:[],V_2:[],N:[]}

k = [1,V_1,V_2,N]
for start in k:
  k =  dji(start,graph)
  L[start] = k

k = [V_1,V_2]
printLists = list(permutations(k, 2))
minum = INF
for printlist in printLists:
  a,b = printlist[0],printlist[1]
  z = L[1][a] + L[a][b] + L[b][N]
  if minum > z:
    minum = z

if minum == INF:
  print(-1)
else:
  print(minum)
