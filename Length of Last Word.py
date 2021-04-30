class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s==" " :
            return 0
        else:
            
            st = s.split(" ")
            st.reverse()
            print(st)
            while len(st[0])<=0:
                del st[0]
                if len(st)==0:
                    return 0
                else:
                    continue
            return len(st[0])



""""

Steps:-
1) Check whether the string is empty or not if it's empty then return 0
2) making a list named st which is equals to s.split(" ")
3)Reversing the list because we have send the length of last word of this list
4)Now in while loop we are check whether the element's length is less than equals to zero or not if it's then it will delete first element from this list
then whether the list is empty or not if it's then it will return 0 otherwise it will iterate again
5) after while loop execution done it will return length of 1st element of st
""""
