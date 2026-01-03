class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ')':'(',
            ']':'[',
            '}':'{',
        }
        stack=[]
        
        for brack in s:
            if brack in close_to_open:
                if stack and stack[-1] == close_to_open[brack]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(brack)                
        return True if not stack else False