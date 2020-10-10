# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur1,cur2 = l1,l2
        result = None
        cur = result
        while(cur1 or cur2):
            value = carry
            if cur1 and cur2:
                value += cur1.val + cur2.val
            elif cur1:
                value += cur1.val
            else:
                value += cur2.val
                
            if value>9:
                carry = 1
                value = value-10
            else:
                carry=0
            
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            
            if not result:
                result = ListNode(value)
                cur = result
            else:
                cur.next = ListNode(value)
                cur = cur.next
        if carry == 1:
            cur.val = value
            cur.next = ListNode(carry)
        return result
            
sol = Solution()
l1 = ListNode(9,ListNode(9,ListNode(9)))
l2 = ListNode(9,ListNode(9))
a = sol.addTwoNumbers(l1,l2)
while(a):
    print(a.val)
    a=a.next