def solution(map):
    w, h = len(map), len(map[0])

    def tryAgain():
        visited = [[False] * h for i in range(w)]
        visited[0][0] = True

        q, i = [(0, 0, 1)], 0
        while i < len(q):
            x, y, length = q[i]
            i += 1
            if x == w - 1 and y == h - 1:
                return length
            
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx >= 0 and nx < w and ny >= 0 and ny < h: # valid coord
                    if map[nx][ny] == 1:
                        continue
                    if visited[nx][ny]:
                        continue
                    visited[nx][ny] = True
                    q.append((nx, ny, length + 1))

        return None # Not solvable

    ans = tryAgain()
    
    for i in range(w):
        for j in range(h):
            if (i, j) in [(0, 0), (w-1, h-1)] or map[i][j] == 0:
                continue
            map[i][j] = 0
            newAns = tryAgain()
            if ans is None or (newAns is not None and ans > newAns):
                ans = newAns
            map[i][j] = 1

    return ans

if __name__ == "__main__":
    import sys

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 15)

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 13)

    print(solution([
        [0, 1],
        [1, 0],
    ]) == 3)

    print(solution([
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
     ]) == 7)

    print(solution([
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]) == 11)