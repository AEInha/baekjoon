from collections import deque
a, b= map(int,input().split())
will_visited_1 = deque([a])
will_visited_2 = []
start =a
visited = set()
s = 0
if a > b:
  print(-1)
elif b%10 != 1 and (b%10)%2 ==1:
  print(-1)
else:
  while True:

    if start == b:
      print(s+1)
      break
    else:
      if not will_visited_1:
        s +=1
        if not will_visited_2:
          print(-1)
          break
        else:
          if min(will_visited_2) > b:
            print(-1)
            break
          else:
            will_visited_1.extend(will_visited_2)
            will_visited_2 = []
      else:
        start = will_visited_1.pop()
        if start in visited:
          continue
        else:
          if 2*start <= b:
            will_visited_2.append(2*start)
          if 10*start + 1 <=b:
            will_visited_2.append(10*start + 1)
          visited.add(start)
