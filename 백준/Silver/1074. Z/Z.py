


def find_z(N,R,C):
  if N <=1:
    if R==0 and C==0:
      return 0
    elif R==1 and C==0:
      return 1
    elif R==0 and C==1:
      return 2
    else:
      return 3
  else:
    if  R <= 2**(N-1)-1 and C <= 2**(N-1)-1:
      return find_z(int(N-1),R,C)
    elif R > 2**(N-1)-1 and C <= 2**(N-1) -1:

      return 2**(2*(N-1)) + find_z(int(N-1),R-2**(N-1),C)
    elif R <= 2**(N-1)-1 and C > 2**(N-1) -1:

      return 2**(2*N -1) + find_z(int(N-1),R,C-2**(N-1))
    else:

      return 3*(2**(2*(N-1))) + find_z(int(N-1),R-2**(N-1),C-2**(N-1))


N,C,R = map(int,input().split())
print(find_z(N,R,C))