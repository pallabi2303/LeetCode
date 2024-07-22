class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Pair the names with the corresponding heights
        people = list(zip(heights, names))

        # Sort the pairs based on heights in descending order
        people.sort(reverse=True, key=lambda x: x[0])
        
        return list(people[i][1] for i in range(len(names)))

