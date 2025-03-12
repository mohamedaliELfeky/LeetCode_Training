class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefx = len(nums) * [1]
        right_prefx = len(nums) * [1]

        for i in range(1, len(nums)):
            left_prefx[i] = left_prefx[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            print(i)
            right_prefx[i] = right_prefx[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            if i == 0:
                nums[i] = right_prefx[i]
            elif i == len(nums) - 1:
                nums[i] = left_prefx[i]

            nums[i] = left_prefx[i] * right_prefx[i]


        return nums
