class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time_arr = []
        for i in range(len(position)):
            pos_time_arr.append((position[i], (target - position[i]) / speed[i]))
        pos_time_arr.sort()

        output = 1
        for i in range(len(pos_time_arr) - 2, -1, -1):
            if pos_time_arr[i][1] > pos_time_arr[i+1][1]:
                output += 1
            else:
                pos_time_arr[i] = (pos_time_arr[i][0], pos_time_arr[i+1][1])
        return output
            
        