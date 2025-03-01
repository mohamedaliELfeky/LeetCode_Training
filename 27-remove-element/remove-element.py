class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index_arr = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                index_arr.append(i)


        for i in index_arr:
            nums.pop(i)