class Solution:
    def twoCityScheduledCost(self, costs:List[List[int]]) -> int: 
        sorted_cost = sorted(costs, key = lambda x:x[0]-x[1])
        result = 0
        
        for i in range(len(costs)):
            if i < len(costs) / 2:
                result += sorted_cost[i][0]
            else:
                result += sorted_cost[i][1]
        
        return result