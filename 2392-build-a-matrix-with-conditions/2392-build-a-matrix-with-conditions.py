from collections import defaultdict, deque
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(graph, k):
            in_degree = [0] * (k + 1)
            for u in graph:
                for v in graph[u]:
                    in_degree[v] += 1

            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            top_order = []

            while queue:
                node = queue.popleft()
                top_order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(top_order) == k:
                return top_order
            else:
                return []
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)

        for above, below in rowConditions:
            row_graph[above].append(below)

        for left, right in colConditions:
            col_graph[left].append(right)

        row_order = topological_sort(row_graph, k)
        col_order = topological_sort(col_graph, k)

        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r = row_pos[num]
            c = col_pos[num]
            matrix[r][c] = num

        return matrix
