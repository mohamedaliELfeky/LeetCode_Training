class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        operations = 0

        total = sum(nums)

        operations = total % k if k <= total else total

        return operations