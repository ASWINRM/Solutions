import sys

DP = [[[sys.maxsize for _ in range(2)] for _ in range(1234)] for _ in range(1234)]
arr = []

def simulate(s, e, f):
    if s > e:
        return 0
    if DP[s][e][f] != sys.maxsize:
        return DP[s][e][f]
    if f:
        DP[s][e][f] = max(simulate(s + 1, e, not f) + arr[s], simulate(s, e - 1, not f) + arr[e])
    else:
        DP[s][e][f] = min(simulate(s + 1, e, not f) - arr[s], simulate(s, e - 1, not f) - arr[e])
    return DP[s][e][f]

def score_difference(tiles):
    global arr
    arr = tiles
    for i in range(1234):
        for j in range(1234):
            DP[i][j][0] = sys.maxsize
            DP[i][j][1] = sys.maxsize
    return simulate(0, len(tiles) - 1, True)

if __name__ == "__main__":
    n = int(input())
    v = []
    for _ in range(n):
        x = int(input())
        v.append(x)
    print(score_difference(v))
