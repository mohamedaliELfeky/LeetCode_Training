from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        counts = Counter(nums)
        ops = 0
        keys_list = list(counts.keys())

        # print(keys_list)
        # print(counts)

        for i in keys_list:

            if i == k-i:
                if counts[i] > 1:
                    divis = counts[i] // 2
                    # counts[i] -= 2 * divis
                    ops += divis
                    
                continue

            
            temp = min(counts[i], counts.get(k - i, 0))
            
            if counts.get(i, 0):
                counts[i] -= temp
            if counts.get(k - i, 0):
                counts[k - i] -= temp

            # print(temp)
            ops += temp
            

        return ops


        

        