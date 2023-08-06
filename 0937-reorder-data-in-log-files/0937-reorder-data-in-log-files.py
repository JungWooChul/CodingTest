class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_log, let_log = [], {}
        
        for i in logs:
            log = i.split(' ')[0]
            words = i.split(' ')[1:]
            if words[0].isdigit():
                dig_log.append(i) 
            else:
                if ' '.join(words) in let_log.keys():
                    let_log[' '.join(words)].append(log)
                else:
                    let_log[' '.join(words)] = [log]
        
        answer = []
        for let in sorted(let_log.keys()):
            for let_tmp in sorted(let_log[let]):
                answer.append(let_tmp+' '+let) # 문자로 구성된 로그는 식별
        answer.extend(dig_log) # 숫자 로그는 입력 순서대로
        
        return answer