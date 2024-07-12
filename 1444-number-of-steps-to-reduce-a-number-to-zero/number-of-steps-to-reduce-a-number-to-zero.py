class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            counter += 1

        return counter
        