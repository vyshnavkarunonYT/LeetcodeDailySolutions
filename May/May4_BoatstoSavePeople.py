class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1

        people.sort()
        l = 0
        r = len(people) - 1
        tot = 0

        while l < r:
            if people[l] + people[r] > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            tot += 1

        if l == r:
            tot += 1

        return tot
