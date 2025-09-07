class Solution:

    def ispair(self, opening, closing):
        return (opening=='(' and closing==')') or \
        (opening=='{' and closing=='}') or \
        (opening=='[' and closing==']')

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if  char in ['[', '(', '{']:
                stack.append(char)
            else:
                if stack and self.ispair(stack[-1], char):
                        stack.pop()
                else:
                    return False
                
        return len(stack)==0
