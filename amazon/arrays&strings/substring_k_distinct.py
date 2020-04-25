# Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
# https://leetcode.com/problems/subarrays-with-k-different-integers

# Example 1:

# Input: s = "pqpqs", k = 2
# Output: 7
# Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
# Example 2:

# Input: s = "aabab", k = 3
# Output: 0
# Constraints:

# The input string consists of only lowercase English letters [a-z]
# 0 ≤ k ≤ 26
from typing import List
from collections import defaultdict
class Solution():
    def subarraysWithKDistinct(self, input: str, k:int ) -> int:

        letters = list(input)

        distinct = set()
        l = r = 0

        # while l < len(letters):

            # If num of distinct is greater than what we're allowed, means we got a char that puts us over our limit
            # if len(distinct) > k:
                # Need to process substring


                # Once done, move left till either substring length is less than k, or number of distinct characters within that substring
                # is k. Reset right to what left is and reset and intialize set()
            

            # distinct.add(letters[r])


            # Search for entire substring
            # Once we get to a violation, then need to process valid substring
            # Leave left and right where they are
            # Process it starting with k lengthed sub-substrings, increasing the sub-substring length till length of entire substring

           

            # Repeat

    def subarraysWithKDistinct2(self, s: str, k: int):

        def mostkChars(s: str, k:int):
            if not len(s):
                return 0
            lookup = defaultdict(int)
            num, left = 0, 0

            for i in range(len(s)):
                lookup[s[i]] += 1
                while len(lookup) > k:
                    lookup[s[left]] -= 1
                    if lookup[s[left]] == 0:
                        del lookup[s[left]]
                    left += 1
                num += i - left + 1
            return num

        res1 = mostkChars(s,k)
        res2 = mostkChars(s, k-1)

        return res1 - res2

s = Solution()
print(s.subarraysWithKDistinct2('pqpqps', 2))
