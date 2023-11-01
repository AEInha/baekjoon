import sys
from collections import deque
def inp():
  return sys.stdin.readline()
  #return input()


N,M = map(int,inp().split())
graph = {i:[] for i in range(1,N+1)}
visited = set(i for i in range(1,N+1))
if M == 0:
  print(N)
elif M == N*(N-1)//2:
  print(1)
else:
  for i in range(M):
    a,b = map(int,inp().split())
    graph[a].append(b)
    graph[b].append(a)


  start = 1
  visited.remove(start)
  will_visited = deque(graph[start])

  answer = 0



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