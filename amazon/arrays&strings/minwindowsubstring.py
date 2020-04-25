from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # answer = ""
        # left = 0
        # right = 0
        # letters = list(t)

        
        # while left <= len(s) - len(t) and right <= len(s): # If we have less letters left in string than target, no way can do this
        #     if all(c in s[left:right] for c in letters):
        #         # Current substring has all letters
                
        #         # Need to see if current substring has a short answer within it (maybe two 'a's)
        #         while left < right:
        #             if all(c in s[left:right] for c in letters) and (answer == "" or len(answer) > len(s[left:right])):
        #                 answer = s[left:right]
        #             left += 1
        #     else:
        #         right += 1
        # return answer

        if not t or not s:
            return ""
        
        # keep track of count of all the unique charcters in t
        dict_t = Counter(t)

        # number of distinct chars in t which need to be in sliding window
        required = len(dict_t)

        l, r = 0, 0
        
        # keep track of number of unique characters in window
        formed = 0

        # keeps track of current window's unique characters
        window_count = {}

        # ans tuple of the form (window length, left, right)
        ans = float('inf'), None, None
        while r < len(s):
            character = s[r]
            # Add one character to the window
            # Could use a default dictionary here
            window_count[character] = window_count.get(character, 0) + 1

            # if the character is one we need to look out for and the number of characters we've seen equals
            # to the target string's characters, then we've satisfied that letter's requirements. Need to look
            # for others (if there are any)
            if character in dict_t and window_count[character] == dict_t[character]:
                formed += 1
            
            # This doesn't get hit unless our current window satisfies the t string
            # Once it does run, it continuously advances left until our window violates
            # the constraint t's letter count
            while l <= r and formed == required:
                character = s[l]

                # Save smallest window
                if r-l+1 < ans[0]:
                    ans = (r-l+1, l, r)
                
                # Remove characters being left behind
                window_count[character] -= 1
                if character in dict_t and window_count[character] < dict_t[character]:
                    formed -= 1
                
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]





s = Solution()
print(s.minWindow("aa","aa"))