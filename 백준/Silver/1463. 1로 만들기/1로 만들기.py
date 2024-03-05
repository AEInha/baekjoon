import sys
def inp():
    #return input()
    return sys.stdin.readline()

def make_one(n):
    dp = {0:[n]}
    current = 0
    visited = {n}
    while True:
        dp[current+1] = []
        for i in dp[current]:

            if i == 1:
                return len(dp)-2
            else:
                visited.add(i)
                if i %2 == 0 and i//2 not in visited:
                    dp[current+1].append(i//2)
                if i %3 == 0 and i//3 not in visited:
                    dp[current+1].append(i//3)
                if i-1 not in visited:
                    dp[current+1].append(i-1)
        current +=1




n = int(inp())
print(make_one(n))

