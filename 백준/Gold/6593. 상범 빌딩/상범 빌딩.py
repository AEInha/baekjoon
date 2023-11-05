
from collections import deque


def simulator(co,L,R,C,matrix):
  b = []
  x = co[2]
  y = co[1]
  z = co[0]
  k = [(z,y,x-1),(z,y,x+1),(z,y+1,x),(z,y-1,x),(z+1,y,x),(z-1,y,x)]

  for i in k:
    if i[0] >= 0 and i[0] <=L-1 and i[1]>=0 and i[1] <= R-1 and i[2] >= 0 and i[2] <= C-1 and matrix[i[0]][i[1]][i[2]] != '#':
        b.append(i)

  return b


def bfs_graph(start,end,matrix):
  visited = set()
  will_visited = deque()
  will_visited.append(start)
  answer =0
  will_visited_2 = []
  L = len(matrix)
  R = len(matrix[0])
  C = len(matrix[0][0])
  while True:

    if will_visited:
      location = will_visited.popleft()
    else:
      if will_visited_2:

        will_visited.extend(will_visited_2)


        will_visited_2 = []
        answer +=1
        location = will_visited.popleft()
      else:
        return False

    if location == end:
      return answer
    else:
      if location in visited:
        continue
      else:
        visited.add(location)
        z = simulator(location,L,R,C,matrix)
        z = list(set(z).difference(visited))
        will_visited_2.extend(z)

  return answer





while True:
  L,R,C  = map(int,input().split())
  if L == 0 and R == 0 and C == 0:
    break
  else:
    matrix = []
    for i in range(L):
      matrix_2 = []
      for j in range(R):
        z = list(input())
        matrix_2.append(z)
        if 'S' in z:
          k = z.index('S')
          start = (i,j,k)
      
        if 'E' in z:
          k = z.index('E')
          end = (i,j,k)
      matrix.append(matrix_2)
      u = input()

    k = bfs_graph(start,end,matrix)
    if k:
      print(f"Escaped in {k} minute(s).")
    else:
      print("Trapped!")
