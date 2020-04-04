# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#1->1->2->2->3
#1->2->2->3

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        n = head
       # m = head.next
        while n:
            if n.next and n.val == n.next.val:
                n.next=n.next.next
            else:
                n=n.next
        return head

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        while p:
            if p.next and p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
