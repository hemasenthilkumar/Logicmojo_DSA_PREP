from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        station_id = 0
        current_gain = 0
        net_gain  = 0

        for i in range(len(gas)):
            net_gain = gas[i] - cost[i]
            
            total_gain += net_gain
            current_gain += net_gain
            if current_gain < 0:
                current_gain = 0
                station_id = i + 1
        
        return station_id if total_gain >=0 else -1