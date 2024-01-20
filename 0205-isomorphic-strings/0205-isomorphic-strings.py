class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_lst = [0]*len(s)
        t_lst = [0]*len(t)
        
        my_dict = {}
        cnt = 0

        s_lst[0]=1
        t_lst[0]=1
        my_dict[s[0]]=t[0]
        
        for i in range (len(s)):
                if s[i] not in my_dict.keys():
                    my_dict[s[i]]=t[i]
        
        my_dict_rev = {}
        for k,v in my_dict.items():
            if v not in my_dict_rev:
                my_dict_rev[v] = k
        
        for i in range(1,len(s)):
            
            if s[i] == s[i-1] and t[i] == t[i-1]:
                s_lst[i] = s_lst[i-1] + 1
                t_lst[i] = t_lst[i-1] + 1
  
            else:
                if t[i] == my_dict[s[i]] and s[i] == my_dict_rev[t[i]]:
                    s_lst[i] =  1
                    t_lst[i] =  1
                else:
                    t_lst[i] = 1000
        print(s_lst,t_lst)
        if s_lst == t_lst:
            return True
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         hash_t = {}
#         for k,v in zip(s,t):
#             if k in hash_t.keys():
#                 if hash_t[k]!=v:
#                     return False
#             else:
#                 if v in hash_t.values():
#                     return False
#                 hash_t[k] = v

#         return True