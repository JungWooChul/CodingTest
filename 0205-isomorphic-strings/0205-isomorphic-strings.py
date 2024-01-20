class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_t = {}
        for k,v in zip(s,t):
            if k in hash_t.keys():
                if hash_t[k]!=v:
                    return False
            else:
                if v in hash_t.values():
                    return False
                hash_t[k] = v

        return True