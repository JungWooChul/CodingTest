class Solution:
    def __init__(self):
        self.answer = []
        self.len = 0
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.len = len(nums)
        self.visited = [0 for _ in range(self.len)]
        
        self.dfs(0, [])
        return self.answer
        
    def dfs(self, cnt, discovered):
        if cnt == len(self.nums):
            self.answer.append(discovered[:])
            return

        for i, val in enumerate(self.nums):
            # 만약 방문했다면 건너 뛰기(순열을 위함)
            if self.visited[i] == 1:
                continue
            # 현재까지의 discovered에 값을 추가하고, 방문 표시하기
            discovered.append(val)
            self.visited[i] = 1

            self.dfs(cnt+1, discovered)
            
            # 방금 전 discovered에 추가한 값과 방문 한 것을 되돌려주기
            discovered.pop()
            self.visited[i] = 0