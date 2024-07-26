class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_count = {}

        # Count the frequency of each row
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_count:
                row_count[row_tuple] += 1
            else:
                row_count[row_tuple] = 1

        # Count the number of matching columns
        count = 0
        for col_index in range(n):
            col_tuple = tuple(grid[row_index][col_index] for row_index in range(n))
            if col_tuple in row_count:
                count += row_count[col_tuple]

        return count
