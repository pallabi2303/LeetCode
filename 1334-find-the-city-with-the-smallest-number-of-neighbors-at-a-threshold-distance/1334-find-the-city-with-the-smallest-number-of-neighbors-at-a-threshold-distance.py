class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distance matrix
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        # Populate the distance matrix with edge weights
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Apply the Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Count the number of reachable cities for each city
        reachable_count = []
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            reachable_count.append(count)

        # Find the city with the smallest number of reachable cities
        # In case of ties, return the city with the greatest number
        min_reachable = min(reachable_count)
        result_city = -1
        for i in range(n):
            if reachable_count[i] == min_reachable:
                result_city = i

        return result_city