"""
Infix to postfix notation
"""
# TC: O(N)
# SC: O(N)

class Solution:
    
    def get_priority(self, operator):
        if operator == "^":
            return 3
        if operator in ['*','/']:
            return 2
        if operator in ['+', '-']:
            return 1
        return 0
    
    def infixtoPostfix(self, s):
        #code here
        postfix = ""
        stack = []
        for i in range(len(s)):
            if s[i].isalnum():
                postfix += s[i]
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == ')':
                while stack and stack[-1] != "(":
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and stack[-1] != '(' :
                    if s[i] == '^':
                        if self.get_priority(s[i]) < self.get_priority(stack[-1]):
                            postfix += stack.pop()
                        else:
                            break
                    else:
                        if self.get_priority(s[i]) <= self.get_priority(stack[-1]):
                            postfix += stack.pop()
                        else:
                            break
                stack.append(s[i])

        while stack :
            postfix += stack.pop()
            
            
        return postfix
        