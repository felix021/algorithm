def BellmanFord(vertices, edges, start):
    distance = { v:float("inf") for v in vertices }
    distance[start] = 0

    for i in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            return None

    return distance

def permutations(arr, n):
    visited = [False] * len(arr)
    ans = []
    p = []
    def solve(i):
        if i == n:
            ans.append(p[:])
            return
        for nxt in range(0, len(arr)):
            if visited[nxt]: continue
            visited[nxt] = True
            p.append(arr[nxt])
            solve(i + 1)
            p.pop()
            visited[nxt] = False
    solve(0)
    return ans


def solution(times, times_limit):
    start = 0
    bulkhead = len(times) - 1
    N = len(times) - 2

    vertices = range(len(times))
    edges = []
    for u, weights in enumerate(times):
        for v, w in enumerate(weights):
            if u == v:
                continue
            edges.append((u, v, w))

    distance = []
    for i in range(len(times)):
        dist_i = BellmanFord(vertices, edges, i)
        if dist_i is None:
            # negative weight loop, means all bunnies can be saved
            return range(len(vertices) - 2)
        distance.append(dist_i)
    
    def check_possible(path):
        fullpath = [start] + path + [bulkhead]
        used = 0
        for i in range(1, len(fullpath)):
            from_p = fullpath[i - 1]
            to_p = fullpath[i]
            used += distance[from_p][to_p]
        return used <= times_limit

    # brute force: check every path to see whether it's possible
    result = [[], [], [], [], [], []]
    bunnies = range(1, N + 1)
    for i in range(1, N + 1):
        for path in permutations(bunnies, i):
            if check_possible(path):
                result[len(path)].append(path)

    while len(result) > 0:
        x = result.pop()
        if len(x) > 0:
            x.sort()
            ans = [i - 1 for i in x[0]]
            ans.sort()
            return ans

    return []

if __name__ == "__main__":
    import sys

    # example case 1
    print (solution([
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]
    ], 1) == [1, 2])
    #sys.exit(0)

    # example case 2
    print (solution([
        [0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0]
    ], 3) == [0, 1])
    #sys.exit(0)

    # example case 1 with large time limit
    print (solution([
        [0, 2, 2, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]
    ], 100) == [0, 1, 2])
    #sys.exit(0)

    # negative loop
    print (solution([
        [0, 2, -10, 2, -1],
        [9, 0, 2, 2, -1],
        [9, 3, 0, 2, -1],
        [9, 3, 2, 0, -1],
        [9, 3, 2, 2, 0]
    ], 100) == [0, 1, 2])
    sys.exit(0)

    print permutations([1,2,3,4,5], 2)
    print permutations([1,2,3,4,5], 3)
    sys.exit(0)