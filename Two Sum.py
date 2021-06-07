class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        for i in nums:
            x=target-i
            if x in nums and i in nums and i!=x:
                # When i and x both are not same & both are present in nums
                return [nums.index(i) , nums.index(x)]
            if i==x and i in nums and nums.count(i)>1:
                # Here i and x are same value
                #here we can't do [nums.index(i) , nums.index(x) ]
                #because both will give same index because i and x are have same value                ind = nums.index(i)
                nums.remove(i)
                ind2= nums.index(x)
                return [ind,1+ind2]
        return [0,0]
