class Solution:
    def canJump(self, nums: List[int]) -> bool:
       
        max_jump = -1
        n = len(nums)

        if n == 1:
            return True

        for i in range(n):

            if nums[i]:
                max_jump = i + nums[i] if max_jump < i + nums[i] else max_jump
            elif (max_jump <= i) and (i != n - 1):
                return False

        return True

