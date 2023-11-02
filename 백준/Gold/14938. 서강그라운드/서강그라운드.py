# 다익스트라 알고리즘
import sys
import heapq
V,m,E = map(int,input().split())
graph = {i:[] for i in range(1,V+1)}
k = list(map(int,input().split()))

item = {i+1:k[i] for i in range(len(k))}

def inp():
  #return input()
  return sys.stdin.readline()

for i in range(E):
  a,b,c = map(int,inp().split())
  graph[a].append((c,b))
  graph[b].append((c,a))


def dijikstra(graph,start):
  distance_list = [sys.maxsize for i in range(1 + len(graph.keys()))]
  distance_list[start] = 0
  location = start
  hp = []
  heapq.heappush(hp,(0,start))
  while hp:
    distance,location  = heapq.heappop(hp)
    if distance_list[location] < distance:
      continue

    for weight in graph[location]:
        cost = distance_list[location]+weight[0]
        if cost < distance_list[weight[1]]:                                     
            distance_list[weight[1]] = cost
            heapq.heappush(hp,(cost,weight[1]))
  
  return distance_list
        

    

answer = 0
for start in graph.keys():
  L = dijikstra(graph,start)
  su = 0
  for i in range(1,len(L)):
    if L[i] <=m:
      su += item[i]
  if answer < su:
    answer = su
print(answer)