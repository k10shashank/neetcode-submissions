from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = dict()
        for i in tasks:
            task_dict[i] = task_dict.get(i, 0) + 1
        
        heap = []
        for i in task_dict:
            heapq.heappush(heap, (-task_dict[i], i))
        
        time = 0
        cooldown = deque()
        queue_items = 0
        for i in range(n):
            cooldown.append(None)


        while len(heap) > 0 or queue_items > 0:
            if len(heap) > 0:
                top = heapq.heappop(heap)
                top = (top[0] + 1, top[1])
                if top[0] < 0:
                    cooldown.append(top)
                    queue_items += 1
                else:
                    cooldown.append(None)
            else:
                cooldown.append(None)

            cool_pop_item = cooldown.popleft()
            if cool_pop_item is not None:
                queue_items -= 1
                heapq.heappush(heap, cool_pop_item)

            time += 1
        
        return time
