class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if ch == "+":
                    stack.append(a + b)
                elif ch == "-":
                    stack.append(a - b)
                elif ch == "*":
                    stack.append(a * b)
                elif ch == "/":
                    # Ensure integer division with truncation towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(ch))
        return stack[-1]