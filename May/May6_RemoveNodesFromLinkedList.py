# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while (temp):
            arr.append(temp.val)
            temp = temp.next

        rightGreater = [False] * len(arr)
        maxSoFar = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] < maxSoFar:
                rightGreater[i] = True
            else:
                maxSoFar = arr[i]

        nHead = ListNode(0)
        temp = nHead

        for i in range(len(arr)):
            if not rightGreater[i]:
                temp.next = head
                temp = temp.next
            head = head.next

        temp.next = None
        return nHead.next