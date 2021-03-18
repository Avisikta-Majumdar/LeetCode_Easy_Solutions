class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss="".join(sorted(s))
        ts="".join(sorted(t))
        #print(ss,ts)
        return ss==ts
        
