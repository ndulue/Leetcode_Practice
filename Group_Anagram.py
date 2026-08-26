class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        for word in strs:
            sortedWords = "".join(sorted(word))
            
            if sortedWords not in dict:
                dict[sortedWords] = word
            
            else:
                dict[sortedWords].append(word)
                
        result = []
        for res in dict:
            result.append(res)
            
        return result    
            