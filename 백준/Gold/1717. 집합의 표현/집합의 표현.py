import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N,M= map(int,input().split())
#union-find
union_set = [i for i in range(N+1)]


def get_parent(x):
  if union_set[x] != x:
    union_set[x] = get_parent(union_set[x])
  return union_set[x]


def union(a,b):
  a = get_parent(a)
  b = get_parent(b)
  parent_node = min(a,b)
  child_node = max(a,b)
  if parent_node == child_node:
    return union_set
  else:
    union_set[child_node] = parent_node
    return union_set


for i in range(M):

  a,b,c = map(int,input().split())
  if a == 0:
    union(b,c)

  elif a == 1:
    if get_parent(b) == get_parent(c):
      print('YES')
    else:
      print('NO') 
