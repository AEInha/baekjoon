
from collections import deque

N,K = map(int,input().split())


#너비우선탐색 사용


def det(n):
  return 0 <= n <= 100000


def bfs(num,target_num):
  will_visited = deque([num])
  visited = set()
  will_visited_2 = []
  answer = 0
  past_dict = [0]*100001
  future_dict =  [0]*100001
  past_dict[num] = 1
  while True:
    if target_num in will_visited:
      break
    else: 
      future_dict = [0]*100001
      will_visited_2 = []
      for location in will_visited:
        if location not in visited:
          visited.add(location)
          A = [i for i in [2*location, location-1, location+1] if det(i)]
          will_visited_2.extend(A)
          for i in A:
            future_dict[i] = future_dict[i] + past_dict[location]
        else:
          A = [i for i in [2*location, location-1, location+1] if det(i)]
          for i in A:
            future_dict[i] = future_dict[i] + past_dict[location]
          continue
      will_visited = list(set(will_visited_2))
      past_dict = future_dict
      answer +=1
  
  return answer,past_dict[K]


if N>=K:
  print(N-K)
  print(1)
else:
    
  answer,L = bfs(N,K)
  print(answer)
  print(L)