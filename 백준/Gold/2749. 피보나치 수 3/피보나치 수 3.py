B = int(input())

A = [[1,1],[1,0]]
N = len(A)



def vector_dot(a,b):
  sum = 0
  for i in range(len(a)):
    sum += a[i]*b[i]
  return sum%1000000


def matrix_multi(A,B):
  d = list(map(list,zip(*B)))
  c = [[0 for i in range(len(A))]for j in range(len(A))] 
  for i in range(len(A)):
    for j in range(len(A)):
      c[i][j] = vector_dot(A[i],d[j])
  return c

def identity_matrix(N):
    result = []
    for i in range(N):
        row = [0] * N 
        row[i] = 1    
        result.append(row)
    return result


a = identity_matrix(N)

def matrix_square(A,N):
  if N == 0:
    return a
  else:
    x = matrix_square(A,N//2)
    if N%2 == 0:
      return matrix_multi(x,x)
    else:
      return matrix_multi(matrix_multi(x,x),A)


if B == 0:
  print(0)
elif B == 1:
  print(1)
else:
  k = matrix_square(A,B-2)
  print((k[0][0]+k[0][1])%1000000)