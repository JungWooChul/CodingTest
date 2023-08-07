class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_log, let_log = [], {}
        
        for i in logs:
            log = i.split(' ')[0]
            words = i.split(' ')[1:]
            # 숫자 로그는 입력 순서대로 저장
            if words[0].isdigit():
                dig_log.append(i) 
            # 문자 로그는 로그를 제외한 부분을 key, 로그를 value로 mapping하여 저장
            else:
                if ' '.join(words) in let_log.keys():
                    let_log[' '.join(words)].append(log)
                else:
                    let_log[' '.join(words)] = [log]
        
        answer = []
        for let in sorted(let_log.keys()): # 로그를 제외한 부분 먼저 정렬
            for let_tmp in sorted(let_log[let]): # 문자가 같다면 로그 정렬
                answer.append(let_tmp+' '+let) # 문자로 구성된 로그는 식별
        answer.extend(dig_log) # 숫자 로그는 입력 순서대로
        
        return answer