class Solution():
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            
            if c == ')':
                # Check stack. If top is a ), then pop it off
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        s_list = list(s)

        while stack:
            del s_list[stack.pop()]

        return "".join(s_list)

test_case_01 = "lee(t(c)o)de)" # -> lee(t(c)o)de
test_case_02 = "a)b(c)d" # -> ab(c)d
test_case_03 = "(a(b(c)d)" # -> a(b(c)d)

s = Solution()
print(s.minRemoveToMakeValid(test_case_01))