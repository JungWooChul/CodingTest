class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_set = ["".join(sorted(list(i))) for i in strs]
        anagrams_dict = {key : [] for key in set(anagrams_set)}
        
        for anagram in strs:
            tmp_key = "".join(sorted(list(anagram)))
            anagrams_dict[tmp_key].append(anagram)
        
        return anagrams_dict.values()
#         anagram_dict = {str : ''.join(sorted(list(str))) for str in strs}
#         # list로는 딕셔너리의 key가 존재하는지 판단 불가능 -> 문자열로 다시 합치기
#         answers = dict()
#         for k, v in anagram_dict.items():
#             if v in answers.keys():
#                 answers[v].append(k)
#             else:
#                 answers[v] = [k]
        
#         answer = [v for v in answers.values()]
#         return answer
          