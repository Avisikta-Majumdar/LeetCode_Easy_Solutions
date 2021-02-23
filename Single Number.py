class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lst=sum(nums)
        set_mult_with_2 = 2*(sum(set(nums)))
        print(set_2,lst)
        return set_2 - lst
    
#nums = [1,2,3,3,2]
#lst = sum(nums)= sum([1,2,3,2,3])----->  11
#set_mult_with_2 = 2*(sum(set(nums)))  -----> 2*sum([1,2,3])=2*6--->  12
#Return the difference between set_mult_with_2 - lst   ---> 12-11 --->1
