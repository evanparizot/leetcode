class Solution:
    def romanToInt(self, s: str) -> int:
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# EX:
# III -> 3
# MCMXCIV -> 1994
# LVIII -> 58
        romans  = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
        result = 0
        chars = list(s)
        for i, c in enumerate(chars):
            # Special cases: IV, IX, XL, XC, CD, CM
            # Can iterate through str. Add letters. If we see combination, then do arithmetic to bring down total
            
            result += romans[c]
            
            if i != 0:
                before = chars[i-1]
                
                if ((c == 'M' and before == 'C') or
                    (c == 'D' and before == 'C') or
                    (c == 'C' and before == 'X') or
                    (c == 'L' and before == 'X') or
                    (c == 'X' and before == 'I') or
                    (c == 'V' and before == 'I')):
                    
                    result -= 2*(romans[before])
        return result

s = Solution()
s.romanToInt('IV')