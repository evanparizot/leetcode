# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(num):
    return num >= 2

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low != high:
            mid = (low + high)//2
            if isBadVersion(mid):
                # If previous is bad version, then need to set bounds
                if not isBadVersion(mid-1):
                    return mid
                else:
                    high = mid
            else:
                low = mid

s = Solution()
s.firstBadVersion(2)