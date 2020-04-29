class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')

        if len(v1) < len(v2):
            v1 = v1 + [0]*(len(v2)-len(v1))
        elif len(v1) > len(v2):
            v2 = v2 + [0]*(len(v1)-len(v2))

        # version1 > version2 : return 1
        # version1 < version2 : return -1
        # return 0 otherwise

        result = 0
        for i in range(len(v1)):
            a = int(v1[i])
            b = int(v2[i])
            if a < b:
                result = -1
                break
            elif a > b:
                result = 1
                break
        
        return result


s = Solution()
s.compareVersion("01","1")