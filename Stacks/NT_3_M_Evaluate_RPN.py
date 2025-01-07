class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
            
        return stack[0]
    
def main():
    inp = ["1","2","+","3","*","4","-"]
    res = Solution()
    print(res.evalRPN(inp))

if __name__ == "__main__":
    main()