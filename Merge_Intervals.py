class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:        
        merged = []
        intervals.sort(key=lambda x: x[0])

        previous = intervals[0]

        for current in intervals[1:]:
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                merged.append(previous)
                previous = current
        
        merged.append(previous)

        return merged 