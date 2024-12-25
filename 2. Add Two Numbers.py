#https://leetcode.com/problems/add-two-numbers/description/
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        
        dummy = ListNode()  
        current = dummy   
        carry = 0   

        
        while l1 or l2 or carry:
             
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

         
            current.next = ListNode(total % 10)   
            carry = total // 10   

            current = current.next   

        return dummy.next 
