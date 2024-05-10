class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        values = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                values.append((arr[i]/arr[j],arr[i],arr[j]))
        values.sort(key = lambda x: x[0])
        k = values[k-1]
        return [k[1],k[2]]