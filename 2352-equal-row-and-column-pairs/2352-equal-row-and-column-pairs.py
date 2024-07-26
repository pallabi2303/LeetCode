class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        co=defaultdict(int)
        n=len(grid)
        matCol=[[] for _ in range(n)]
        for i in range(n):
            for j in range(len(grid[0])):
                matCol[i].append(grid[j][i])
        for i in grid:
            if i in matCol:
                count+=matCol.count(i)
        return count
        