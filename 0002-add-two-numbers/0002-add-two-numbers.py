# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize dummy node and current pointer
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2:
            # Get the values from the current nodes or use 0 if a list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Create a new node with the sum and add it to the result
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move to the next nodes
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        # If there's still a carry left, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next of dummy node which is the head of the resultant list
        return dummy.next

        