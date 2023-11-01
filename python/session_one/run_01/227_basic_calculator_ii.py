class Solution():

    def calculate(self, s):
        stack, num, sign = [], 0, '+'

        for i in range(len(s)):
            if s[i].isdigit():
                num = (num*10) + int(s[i])
            elif s[i] in '+-*/' or i == len(s) -1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop()*num)
                if sign == '/':
                    p = stack.pop()
                    res = abs(p) // num
                    stack.append(res if p >= 0 else -res)
                num = 0
                sign = s[i]
        return sum(stack)