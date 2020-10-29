
INF = float("inf")

class Solution(object):
    def networkDelayTimeBFS(self, times, N, K):
        g = {}
        for u, v, w in times:
            if u not in g:
                g[u] = []
            g[u].append((v, w))

        distance = {}
        q = [(K, 0)]
        idx = 0
        while idx < len(q):
            u, d = q[idx]
            idx += 1
            distance[u] = d
            for v, w in g.get(u, []):
                if d + w >= distance.get(v, INF):
                    continue
                q.append((v, d + w))
        
        if len(distance) != N:
            return -1
        
        return max(distance.values())

    def networkDelayTimeDijkstra(self, times, N, K):
        g = {}
        distance = {K: 0}
        for u, v, w in times:
            if u not in g:
                g[u] = []
            g[u].append((v, w))
            if u == K:
                distance[v] = min(distance.get(v, INF), w)

        all = set(range(1, N + 1))
        visited = set([K])
        candidates = all - visited

        while len(visited) < N:
            next = None
            for v in candidates:
                if v in distance and distance[v] < distance.get(next, INF):
                    next = v
            
            if next is None:
                return -1

            visited.add(next)
            candidates.remove(next)

            for v, w in g.get(next, []):
                if distance[next] + w < distance.get(v, INF):
                    distance[v] = distance[next] + w
            
        return max(distance.values())

    def networkDelayTimeBellmanFord(self, times, N, K): 
        distance = {}
        predecessor = {}
        for v in range(1, N + 1):
            if v == K:
                distance[v] = 0
            else:
                distance[v] = INF
            predecessor[v] = None

        for i in range(1, N):
            for u, v, w in times:
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    predecessor[v] = u
        
        for u, v, w in times:
            if distance[u] + w < distance[v]:
                return -1 # negative weight loop

        result = max(distance.values())
        if result == INF:
            return -1
        return result



if __name__ == "__main__":
    s = Solution()
    print (s.networkDelayTimeBellmanFord([
        [2,1,1],
        [2,3,1],
        [3,4,1]
    ], 4, 2) == 2)
    """
        2   -1->    1
            -1->    3    -1->   4
    """