class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        temp = nums1[:m]

        l1, l2 = len(temp), len(nums2)
        p1, p2, p_o = 0, 0, 0

        while p1 < l1 and p2 < l2:
            if temp[p1] <= nums2[p2]:
                nums1[p_o] = temp[p1]
                p1 += 1
            
            else:
                nums1[p_o] = nums2[p2]
                p2 += 1

            p_o += 1

        if p1 < l1:
            for elmnt in temp[p1:]:
                nums1[p_o] = elmnt
                p_o +=  1

        elif p2 < l2:
            for elmnt in nums2[p2:]:
                nums1[p_o] = elmnt
                p_o +=  1



        