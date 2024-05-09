# Priority Queue implementation - Much worse than sort implementation
from queue import PriorityQueue
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happy = PriorityQueue()
        for val in happiness:
            happy.put(-val)

        total = 0
        for i in range(k):
            total += max(0, -happy.get() - i)

        return total
