class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = list(set(nums1) - set(nums2))
        l2 = list(set(nums2) - set(nums1))

        return list((l1, l2))