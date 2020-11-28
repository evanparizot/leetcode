class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1 # 1 = +, -1 = -

        for c in s:
            if c.isdigit():
                # forming operand, could be more than one digit
                operand = (operand*10) + int(c)
            elif c == '+':
                # Evalutate the expression to the left, with result, sign, operand
                res += sign * operand

                # Save the recently encountered +
                sign = 1

                # Reset
                operand = 0
            elif c == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif c == '(':
                # Push these onto the stack for later
                stack.append(res)
                stack.append(sign)

                # Reset operand and sign (for sub-expression)
                sign = 1
                res = 0
            elif c == ')':
                # Evaluate the expression to the left with result, sign and operand
                res += sign * operand

                # ')' marks the end of an expression within a set of parenthesis.
                # It's result is multiplied with sign on top of the stack as stack.pop()
                # is the sign before the parenthesis
                res *= stack.pop()

                res += stack.pop()

                operand = 0
            
        return res + sign * operand

s = Solution()
s.calculate("(1+( 4+5+2)-3) +(6+8)")