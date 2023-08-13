class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_set = ["".join(sorted(list(i))) for i in strs]
        anagrams_dict = {key : [] for key in set(anagrams_set)}
        
        for anagram in strs:
            anagrams_dict["".join(sorted(list(anagram)))].append(anagram)
        
        return anagrams_dict.values()
          