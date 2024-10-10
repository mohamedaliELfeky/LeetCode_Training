class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        prefix_sum = [nums[-1]]
        temp_sum = 0

        for i, num in enumerate(reversed(nums[:-1])):
            prefix_sum.append(prefix_sum[i] + num)

        prefix_sum = prefix_sum[::-1]
        
        for i, num in enumerate(nums):
            temp_sum += num
            if temp_sum == prefix_sum[i]:
                return i

        return -1

