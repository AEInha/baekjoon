import sys
import heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())
graph = {i:[] for i in range(1,N+1)}
for i in range(M):
  u,v,w = map(int,input().split())
  graph[u].append((w,v))


def dij(graph,start):
  distance = [sys.maxsize]*(len(graph)+1)
  distance[start] = 0
  hp = []
  location = start
  heapq.heappush(hp,(0,location))
  while hp:
    dist, location = heapq.heappop(hp)
    if dist > distance[location]:
      continue
    for weight in graph[location]:
      cost = weight[0] + distance[location]
      if cost < distance[weight[1]]:
        distance[weight[1]] = cost
        heapq.heappush(hp,(cost,weight[1]))
  return distance


max_num = 0
k = dij(graph,X)
for start in range(1,N+1):
  L = dij(graph,start)
  if max_num < L[X]+ k[start]:
    max_num = L[X] + k[start]

print(max_num)
