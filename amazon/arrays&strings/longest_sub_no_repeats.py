class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        seen = set()
        longest_seen = 0
        l, r = 0, 0

        while r < len(s):
            character = chars[r]

            # character is in set, need to move left pointer removing characters until we satisfy uniqueness
            while character in seen:
                seen.remove(chars[l])
                l += 1
            else:
                # Add current character back once we're done
                seen.add(character)

            longest_seen = max(longest_seen, r-l+1)
            r += 1
        
        return longest_seen


s = Solution()
print(s.lengthOfLongestSubstring("bbbbbb"))
print(s.lengthOfLongestSubstring("abcabcbb"))