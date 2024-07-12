# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_count = 1
        position = head

        while position.next:
            node_count += 1
            position = position.next
        
        # print(node_count)
        node_count = node_count // 2 + 1
        # print(node_count)

        for _ in range(node_count  - 1):
            head = head.next

        return head