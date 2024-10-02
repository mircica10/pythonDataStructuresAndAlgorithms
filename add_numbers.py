"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
delete comment hier 20241003
"""

# Definition for singly-linked list. 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers( self, l1, l2 ):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l = []
        
        while not l1 is None and not l2 is None:
            current_number = l1.val + l2.val + carry
            carry = current_number // 10
            current_digit = current_number % 10 
            
            l.append( current_digit )
            
            l1 = l1.next
            l2 = l2.next
        #we check is there are remaining digits in one of the lists
        remaining_l = l2 if l1 is None else l1
        
        while not remaining_l is None :
            current_number = remaining_l.val + carry
            carry = current_number // 10
            current_digit = current_number % 10
            
            l.append(current_digit)    
            
            remaining_l = remaining_l.next
        
        if carry > 0:
            l.append(carry)
        
        return l

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
def test():
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(6)
    l1.next.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    result = sol.addTwoNumbers(l1,l2)
    assert( result == [7,0,1,4] )

test()

