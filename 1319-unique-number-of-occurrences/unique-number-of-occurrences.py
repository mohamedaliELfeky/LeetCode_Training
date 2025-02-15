class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        unique_nums = dict()

        for num in arr:
            unique_nums[num] = unique_nums.get(num, 0) + 1

        return len(set(unique_nums.values())) == len(unique_nums.values()) 