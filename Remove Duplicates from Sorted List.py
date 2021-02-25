#Made 1 list and there storing all the no present in linkedlist
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l=[]
        temp = head
        prev = None
        while temp:
            if temp.val in l:# This means temp.val is occuring 2nd time in this LinkedList
                prev.next = temp.next
                temp = temp.next
            else:
                l.append(temp.val)
                prev = temp
                temp = temp.next  
                
        return head
