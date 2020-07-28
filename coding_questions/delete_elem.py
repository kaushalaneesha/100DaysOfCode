# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int) -> ListNode:
    if not head:
        return
    curr = head.next
    prev = head
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    if head.val == val:
        return head.next
    else:
        return head

# Test case:
# [1,2,6,3,4,5,6]
# 6