class Solution:
        def sortArray(self, arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr

            # Finding the mid of the array
            mid = len(arr) // 2

            # Dividing the elements into 2 halves
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Sorting the first and second halves
            left_half = self.sortArray(left_half)
            right_half = self.sortArray(right_half)

            return self.merge(left_half, right_half)

        def merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
            i = j = k = 0
            sorted_array = []

            # Copy data to temp arrays left_half[] and right_half[]
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    sorted_array.append(left_half[i])
                    i += 1
                else:
                    sorted_array.append(right_half[j])
                    j += 1
                k += 1

            # Checking if any element was left
            while i < len(left_half):
                sorted_array.append(left_half[i])
                i += 1
                k += 1

            while j < len(right_half):
                sorted_array.append(right_half[j])
                j += 1
                k += 1

            return sorted_array