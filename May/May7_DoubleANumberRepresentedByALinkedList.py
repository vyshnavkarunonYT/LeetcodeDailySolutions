# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while (temp):
            arr.append(temp.val)
            temp = temp.next

        carry = 0
        for i in range(len(arr) - 1, -1, -1):
            tot = carry + arr[i] * 2
            arr[i] = tot % 10
            carry = tot // 10

        if carry != 0:
            arr.insert(0, carry)

        temp = head
        i = 0 if carry == 0 else 1
        while (temp):
            temp.val = arr[i]
            i += 1
            temp = temp.next

        if carry != 0:
            newHead = ListNode(carry)
            newHead.next = head
            head = newHead

        return head
