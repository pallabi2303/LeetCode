class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Calculate the frequency of each number
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # Sort the nums array with custom key
        nums.sort(key=lambda x: (frequency[x], -x))

        return nums