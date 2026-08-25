class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s == "":
            return ""
        
        if len(s) == 1:
            return s
        
        rev = s[::-1]
        res = ""
        
        for i in range(len(s)):
            if s[i] == rev[i]:
                res += res
                
        return res
    
    