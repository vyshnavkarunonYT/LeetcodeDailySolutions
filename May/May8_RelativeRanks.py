class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        posScores = [(i,v) for i,v in enumerate(score)]
        posScores.sort(key=lambda x: x[1], reverse = True)
        res = [''] * len(posScores)

        for i in range(len(posScores)):
            pos = posScores[i][0]
            if i == 0:
                res[pos] = 'Gold Medal'
            elif i==1:
                res[pos] = 'Silver Medal'
            elif i==2:
                res[pos] = 'Bronze Medal'
            else:
                res[pos] = str(i+1)
        return res

