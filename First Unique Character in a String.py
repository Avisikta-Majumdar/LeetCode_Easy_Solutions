class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==0:
            return -1
        elif len(s)==1:
            return 0
        else:
            n=s
            lst=[i for i in s]
           # print(lst)
            d=Counter(lst) 
          #  print(d)
            for i in range(len(lst)):
                v= lst[i]
                if d[v]==1:
                    return i
            return -1
        
        
        
        """steps:-
        1)check whether the strin g is less than 2 then 
                i)make a list with all the char available in this string 
                ii)Using Counter count which letter occur how many times & make a dictionary of it
                iii)Use for loop to check one by one  if the lst[i] is occured once then return its index value
                iv) if no list element occured once then return -1"""
            
        
