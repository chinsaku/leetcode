# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1


        origin = ListNode(0)
        #.next = None
        outcome = origin
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                origin.next = l2
                l2 = l2.next
            else:
                origin.next = l1
                l1 = l1.next
            origin = origin.next
        if l1 == None:
            origin.next = l2
        if l2 ==None:
            origin.next = l1
            
        return outcome.next


'''
.next指向的是一个节点
同时要注意保留指针，指针指向初始
'''