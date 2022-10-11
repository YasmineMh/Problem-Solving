class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                digit = i
            else:
                lastDigit = int(stack.pop())
                beforeLastDigit = int(stack.pop())
                if i == "+":
                    digit = beforeLastDigit + lastDigit
                elif i == "-":
                    digit = beforeLastDigit - lastDigit
                elif i == "*":
                    digit = beforeLastDigit * lastDigit
                elif i == "/":
                    digit = int(beforeLastDigit / lastDigit)
            stack.append(digit)
        
        return stack[0]