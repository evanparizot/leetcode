from collections import OrderedDict
class Solution():
    def firstUniqChar(self, s: str) -> int:

        # 'a': (#seen, [indicies])

        # 'a': (1st index, is_unique)

        unique = OrderedDict()
        for i, c in enumerate(list(s)):

            # If character already in unique, means that we can't use it
            if c in unique:
                unique[c] = (unique[c][0], False)
            else:
                unique[c] = (i, True)
        
        for key, value in unique.items():
            if value[1]:
                return value[0]
        
        return -1

s = Solution()
s.firstUniqChar('z')