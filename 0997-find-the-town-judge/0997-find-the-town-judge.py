from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        discovered = defaultdict(list)
        for i in trust:
            discovered[i[1]].append(i[0])
        
        for k,v in discovered.items():
            if len(v) == n-1:
                for i in v:
                    if k in discovered[i]:
                        return -1
                return k
            
        return n if n==1 else -1
        