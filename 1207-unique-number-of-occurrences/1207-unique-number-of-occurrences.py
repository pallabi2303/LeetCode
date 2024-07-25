class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        x = Counter(arr)
        values = list(x.values())
        unique = set(x.values())
        return len(values)==len(unique)
            
            
        