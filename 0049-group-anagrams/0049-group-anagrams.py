class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_set = ["".join(sorted(list(i))) for i in strs]
        anagrams_dict = {key : [] for key in set(anagrams_set)}
        
        for anagram in strs:
            tmp_key = "".join(sorted(list(anagram)))
            anagrams_dict[tmp_key].append(anagram)
        
        return anagrams_dict.values()
          