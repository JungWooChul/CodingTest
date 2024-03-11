from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 구성
        graph = {(i+1):{} for i in range(n)}
        for i in times:
            graph[i[0]][i[1]] = i[2]
        
        # 최단 거리 저장
        distances = {node:float('inf') for node in graph}
        distances[k] = 0
        
        # 우선순위 큐 선언
        queue = []
        heapq.heappush(queue, [distances[k], k])  # 시작 노드부터 탐색 시작 하기 위함.
            
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if graph[current_node] == {} or distances[current_node] < current_distance:  
                # 더 이상 이동할 노드가 없거나 기존에 있는 거리보다 길다면 볼 필요 없음
                continue
            for new_node, new_distance in graph[current_node].items():
                distance = new_distance + current_distance # 해당 노드를 거쳐 갈 때 거리
                if distances[new_node] > distance: # 알고 있는 거리 보다 작으면 갱신
                    distances[new_node] = distance
                    heapq.heappush(queue, [distance, new_node])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        
        if max(distances.values()) == float('inf'):
            return -1
        else:
            return max(distances.values())