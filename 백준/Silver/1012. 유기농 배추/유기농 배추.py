import sys
from collections import deque
def inp():
  #return sys.stdin.readline()
  return input()

T = int(inp())
for i in range(T):
  M,N,K = map(int,inp().split())
  if K !=1:
    dps = []
    save_dp = [[0 for i in range(M)] for j in range(N)]

    k = {}
    for i in range(K):
      X,Y = map(int,inp().split())
      dps.append([Y,X])
      save_dp[Y][X] =1
      k[M*Y+X] = set()



    for dp in dps:
      Y,X = dp[0],dp[1]
      up = Y-1
      down = Y+1
      left =X-1
      right = X+1
      if up >=0:
        if save_dp[up][X] == 1:
          k[M*Y+X].add(M*up+X)
          k[M*up+X].add(M*Y+X)
      if down <=N-1:
        if save_dp[down][X] == 1:
          k[M*Y+X].add(M*down+X)
          k[M*down+X].add(M*Y+X)
      if left >= 0:
        if save_dp[Y][left] == 1:
          k[M*Y+X].add(M*Y+left)
          k[M*Y+left].add(M*Y+X)
      if right <=M-1:
        if save_dp[Y][right] == 1:
          k[M*Y+X].add(M*Y+right)
          k[M*Y+right].add(M*Y+X)


    answer = 0
    

    graph = {}

    for element in k:
      if len(k[element])!=0:
        graph[element] = list(k[element])
      if len(k[element]) == 0:
        answer +=1


    visited = set(graph.keys())

    if visited:

      start = list(visited)[0]
      visited.remove(start)
      will_visited = deque(graph[start])
      while True:

        if not visited:
          answer+=1
          break
        else:
          if not will_visited:
            start = list(visited)[0]
            visited.remove(start)
            answer+=1
            will_visited.extend(graph[start])
          else:
            start = will_visited.pop()
            visited.remove(start)
            A = set(graph[start]).intersection(visited)
            will_visited.extend(list(A))
            will_visited = list(set(will_visited).intersection(visited))


      print(answer)
    else:
      print(answer)
  else:
    asdffsfdsf = input()
    print(1)

