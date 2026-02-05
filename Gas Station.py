class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # If we run out of gas, reset the starting point
            if tank < 0:
                start = i + 1
                tank = 0

        return start
