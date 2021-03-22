# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        temp=head
        lst=[]
        while temp:
            value = temp.val
            lst.append(value)
            temp=temp.next
        for i in range(len(lst)//2):
            if lst[i]==lst[len(lst)-1-i]:
                continue
            else:
                return 0
        return 1
    
    """steps:-
    i)Make a list called lst
    ii)take one by one value from SLL and append it to lst
    iii) Do for loop with range (len(lst)//2) check 1st ele. with last ele of that list like that 
    iv) If cond. true then return 1 otherwise return 0"""
        
