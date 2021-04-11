class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return 1
        if n<=0:
            return 0
        else:
            return Solution.isPowerOfTwo(self , n/2)
        
        
        
        """steps:-
        1)here we will use recursion 
        2) each time n will be divided by 2 &will call this isPowerOfTwo 
        3) if n is power of 2 then it will return 1 once.
        
        
        """
