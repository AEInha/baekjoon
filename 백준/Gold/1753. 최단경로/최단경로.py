import heapq
import sys


INF = sys.maxsize

input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

graph = {i:[] for i in range(1,V+1)}

for i in range(E):
  u,v,w = map(int,input().split())
  graph[u].append((w,v))


def dijikstra(graph,start):
  distance = [INF for i in range(1 + len(graph.keys()))]
  distance[start] = 0
  location = start
  hp = []
  heapq.heappush(hp,(0,start))
  while hp:
    dist,location  = heapq.heappop(hp)
    if distance[location] < dist:
      continue
    for weight in graph[location]:
      cost = weight[0] + distance[location]
      if cost < distance[weight[1]]:
        distance[weight[1]] = cost
        heapq.heappush(hp,(cost,weight[1]))
  return distance


if V == 1:
  print(0)
else:
  L = dijikstra(graph,start)
  for i in range(1,len(L)):
    if L[i] == INF:
      print('INF')
    else:
      print(L[i])