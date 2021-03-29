class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #Method1
        Length = len(nums)
        lst =[i for i in range(0,1+Length)]
        return sum(lst)- sum(nums)




'''
Steps:-
1) Finding the length
2)making lst this lst will contain all the element of range(0,1+Length)
3) Subtracting lst by nums this will give us the missing element value.
Example :-
nums=[0,2,3]
lst=[0,1,2,3]
returning sum(lst) - sum(nums)--->  (6 - 5)  -->   1

'''
