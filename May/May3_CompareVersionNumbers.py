class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        for i in range(min(len(v1), len(v2))):
            val1 = int(v1[i])
            val2 = int(v2[i])
            if val1 > val2:
                return 1
            if val2 > val1:
                return -1

        if len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                if int(v1[i]) != 0:
                    return 1
        else:
            for i in range(len(v1), len(v2)):
                if int(v2[i]) != 0:
                    return -1

        return 0