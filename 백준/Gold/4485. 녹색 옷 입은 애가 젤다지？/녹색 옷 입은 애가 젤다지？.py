import heapq
import sys
INF = sys.maxsize




def possible_location(L,N):
  Y,X = L[0],L[1]
  if Y >=0 and Y<=N-1 and X>=0 and X<=N-1:
    return (Y,X)
  else:
    return False






def dji(start,graph):
  distance = [INF]*len(graph)*len(graph)
  hp = []
  N = len(graph)
  heapq.heappush(hp,(graph[start[0]][start[1]],start))
  distance[N*start[0]+start[1]] = graph[start[0]][start[1]]
  
  while hp:
    w,v = heapq.heappop(hp)
    if w > distance[N*v[0]+v[1]]:
      continue
    else:
      locations = [i for i in [(v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)] if possible_location(i,N)]
      for location in locations:
        w_2 = graph[location[0]][location[1]]
        cost = w_2+ w
        if cost < distance[N*location[0]+location[1]]:
          distance[N*location[0]+location[1]] = cost
          heapq.heappush(hp,(cost,location))

  return distance[N**2 -1]

N = 1
s = 1
while N !=0:
  #사다리의 수 N, 뱀의 수 M 입력 받기 
  N= int(input())
  if N == 0:
    break
  graph = []
  for i in range(N):
    graph.append(list(map(int,input().split())))
  a = dji((0,0),graph)
  print(f"Problem {s}: {a}")
  s +=1