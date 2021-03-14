class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(s)) 
        t = ''.join(sorted(t))
        s+="0"
        for i in range(len(t)):
            if s[i]==t[i]:
                continue 
            else:
                return t[i]
