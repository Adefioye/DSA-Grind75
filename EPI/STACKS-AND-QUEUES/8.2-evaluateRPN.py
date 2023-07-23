class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "/", "*"]
        stack = []

        for token in tokens:

            if token not in operators:
                stack.append(token)
            else:
                first = stack.pop()
                second = stack.pop()
                res = eval(f"{second} {token} {first}")

                if token == "/":
                    if res > 0:
                        stack.append(str(math.floor(res)))
                    else:
                        stack.append(str(math.ceil(res)))
                else:
                    stack.append(str(res))
        
        return int(stack[0])