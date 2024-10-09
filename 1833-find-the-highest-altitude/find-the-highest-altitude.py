class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_gain = float('-inf')
        prefix_sum = [0]

        for i, num in enumerate(gain):
            prefix_sum.append(prefix_sum[i] + num)

        return max(prefix_sum)
             