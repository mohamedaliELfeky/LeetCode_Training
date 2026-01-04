class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for elm in nums:

            if elm  % 3 != 0:
                # remiander = (elm / 3) - (elm // 3)
                # operations += 1 if remiander >= 0.5 else -1
                operations += 1

        return operations