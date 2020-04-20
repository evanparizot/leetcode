class Solution():
  def intToRoman(self, num: int) -> str:
    romans  = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M': 1000}

    ints_romans = {1:'I', 5:'V', 10:'X', 50: 'L', 'C': 100, 500:'D', 1000:'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
          (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    # I can be placed before V (5) and X (10) to make 4 and 9. 
    # X can be placed before L (50) and C (100) to make 40 and 90. 
    # C can be placed before D (500) and M (1000) to make 400 and 900.
    result = ''
    # need to account for powers of 10 for 4 and 9
    # IV = 4
    # IX = 9
    # XL = 40
    # XC = 90
    # CD = 400
    # CM = 900

    # 1090

    # 1990

    # 1000 + 900 + 90 + 0
    # 1994
    # 1000 + 900 + 90 + 4

    roman_digits = []
    # Loop through each symbol.
    for value, symbol in digits:
        # We don't want to continue looping if we're done.
        if num == 0: break
        count, num = divmod(num, value)
        # Append "count" copies of "symbol" to roman_digits.
        roman_digits.append(symbol * count)
    return "".join(roman_digits)

    # 58
    # 50 + 8
    # numbers = [int(d) for d in str(num)]
    # for i, n in enumerate(numbers):
    #   p = n * (10 ** (len(numbers) - 1 -i ))

    #   if p in ints_romans:
    #     result += ints_romans[p]
    #     continue

    #   while p > 0:
    #     if p % 1000 == 0:
    #       p -= 1000
    #       result += 'M'
        
    #     elif p - 500 >= 0:
    #       p -= 500
    #       result += 'D'
        
    #     elif p - 100 >= 0:
    #       p -= 100
    #       result += 'C'

    #     elif p - 50 >= 0:
    #       p -= 50
    #       result += 'L'
        
    #     elif p - 10 >= 0:
    #       p -= 10
    #       result += 'X'

    #     elif p - 5 >= 0:
    #       p -= 5
    #       result += 'V'

    #     elif p - 1 >= 0:
    #       p -= 1
    #       result += 'I'

s = Solution()
s.intToRoman(3724)