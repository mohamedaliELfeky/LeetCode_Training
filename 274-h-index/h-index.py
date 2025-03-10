class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        largest_h = 0
        for h in range(len(citations)):

            if citations[h] >= h + 1:
                largest_h = h + 1
            else:
                break

        return largest_h
            