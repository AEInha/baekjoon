import heapq
import sys
INF = sys.maxsize


from collections import deque
import sys

input = sys.stdin.readline

#사다리의 수 N, 뱀의 수 M 입력 받기 
N,M = map(int,input().split())
graph = {}




for i in range(N+M):
  #뱀과 사다리는 그저 단방향 연결 리스트일 뿐이다
  u,v = map(int,input().split())
  graph[u] = v


def make_possible(X):
  return [i for i in range(min(X+1,100),min(X+7,101))]



def possible_with_graph(X,graph):
  if X in graph.keys():
    return graph[X]
  else:
    return X


def dji(start,graph):
  distance = [INF]*101
  hp = []
  heapq.heappush(hp,(0,start))
  distance[start] = 0
  while hp:

    w,v = heapq.heappop(hp)
    if w > distance[v]:
      continue
    else:
      possible_list = make_possible(v)

      possible_list = [possible_with_graph(i,graph) for i in possible_list]

      for possible in possible_list:
        cost = w +1
        if distance[possible] > cost:
          distance[possible] = cost
          heapq.heappush(hp,(cost,possible))

  return distance


a = dji(1,graph)
print(a[100])