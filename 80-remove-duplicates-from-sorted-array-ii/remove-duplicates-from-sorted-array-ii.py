class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        temp_index = []
        temp_num = nums[-1]
        temp_count = 1

        for indx in reversed(range(len(nums) - 1)):
            if nums[indx] == temp_num and temp_count >= 2:
                temp_index.append(indx)

            elif nums[indx] == temp_num:
                temp_count += 1

            else:
                temp_num = nums[indx]
                temp_count = 1

        for elmt in temp_index:
            nums.pop(elmt)

        return len(nums)