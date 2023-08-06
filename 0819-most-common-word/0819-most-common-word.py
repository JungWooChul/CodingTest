class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        tmp_lst = []
        
        # paragraph 분리
        for i in paragraph.replace(',',' ').split(' '):
            tmp = re.sub('[^a-zA-Z]','',i) # 단어에서 영어만 남기기
            tmp_lst.append(tmp.lower()) # 소문자로 저장
        
        # 금지된 단어가 아닌 단어만 포함
        tmp_lst = [tmp for tmp in tmp_lst if tmp not in banned]
        
        # 단어 - 단어 횟수 mapping
        count_dict = {i:0 for i in set(tmp_lst)}
        for i in tmp_lst:
            count_dict[i] += 1
    
        # 정답 고르기
        max = 0
        for k,v in count_dict.items():
            if max < v and len(k)>0:
                answer = k
                max = v
        
        return answer