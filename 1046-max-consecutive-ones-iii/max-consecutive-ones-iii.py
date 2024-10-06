class Solution:

    def with_k(self, nums, k):
        ques = []
        counter = 0
        max_counter = 0
        temp_k = k

        for i, num in enumerate(nums):

            if num:
                counter += 1
            elif temp_k > 0:
                temp_k -= 1
                counter += 1
                ques.append(i)
            else:
                ques.append(i)
                max_counter = max(max_counter, counter)
                counter = i - ques.pop(0)

        return max(max_counter, counter)

    def no_k(self, nums):
        max_count = 0
        temp_max = 0
        for num in nums:
            if num:
               temp_max += 1
            else:
                max_count = max(max_count, temp_max)
                temp_max = 0

        return max(max_count, temp_max)

    def longestOnes(self, nums: List[int], k: int) -> int:
        

        if nums.count(1) == len(nums):
            return len(nums)

        
        if k:
            return self.with_k(nums, k)
        
        return self.no_k(nums)




