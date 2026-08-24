class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:        
        if len(strs) == 0:
            return ""
        
        minlen = len(strs[0])
        for i in range (len(strs)):
            minlen = min(len(strs[i]), minlen)
        
        lcp = ""
        i = 0
        
        while i < minlen:
            char = strs[0][i]
            for j in range(1, len(str)):
                if char != strs[j][i]:
                    return lcp
            lcp = lcp + char           
            i += 1
        
        return lcp
        