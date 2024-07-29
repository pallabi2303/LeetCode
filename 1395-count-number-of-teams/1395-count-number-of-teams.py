class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        # Arrays to store the counts
        left_less = [0] * n
        left_greater = [0] * n
        right_less = [0] * n
        right_greater = [0] * n

        # Count for left part
        for j in range(1, n):
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less[j] += 1
                elif rating[i] > rating[j]:
                    left_greater[j] += 1

        # Count for right part
        for j in range(n - 2, -1, -1):
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    right_greater[j] += 1
                elif rating[j] > rating[k]:
                    right_less[j] += 1

        # Calculate the number of valid teams
        count = 0
        for j in range(n):
            count += left_less[j] * right_greater[j] + left_greater[j] * right_less[j]

        return count
