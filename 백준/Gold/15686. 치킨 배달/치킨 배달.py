import itertools
import sys
chickens = []
houses = []
N,M = map(int,input().split())
for i in range(N):
  L = list(map(int,input().split()))
  for j in range(len(L)):
    if L[j] == 1:
      houses.append([i,j])
    elif L[j] == 2:
      chickens.append([i,j])
    else:
      continue

chicken_list = []
possible_chickens = list(itertools.combinations(chickens, M))
def length(a,b,N):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])

answer = sys.maxsize

for chickens in possible_chickens:
  z = 0
  for house in houses:
    k = 2*N
    for chicken in chickens:
      a = length(house,chicken,N)
      if a < k:
        k = a
      else:
        continue
    z += k
  if answer >z:
    answer = z
  


print(answer)