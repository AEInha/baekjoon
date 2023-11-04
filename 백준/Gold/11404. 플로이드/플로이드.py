
import sys
import heapq


input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
K = int(input())
graph = {i:[] for i in range(1,N+1)}
for i in range(K):
  u,v,w = map(int,input().split())
  graph[u].append([v,w])




def dij(start,graphs):
  hp = []
  heapq.heappush(hp,(0,start))
  distance = [INF]*(len(graphs)+1)
  distance[start] = 0
  while hp:
    w_1,v_1 = heapq.heappop(hp)
    if w_1 > distance[v_1]:
      continue
    else:
      for graph in graphs[v_1]:
        v_2,w_2 = graph[0],graph[1]
        cost = w_2 + w_1
        if cost < distance[v_2]:
          distance[v_2] = cost
          heapq.heappush(hp,(cost,v_2))
  return distance

for start in range(1,N+1):
  L = dij(start,graph)[1:]
  print(*[i if i != INF else 0 for i in L])