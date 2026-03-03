class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_num = []
        oper = ['+','-','*','/']

        for i in tokens:
            if i not in oper:
                stack_num.append(int(i))
            else:
                num1 = stack_num.pop()
                num2 = stack_num.pop()
                if i == '+':
                    stack_num.append(num2+num1)
                elif i == '-':
                    stack_num.append(num2-num1)
                elif i =='*':
                    stack_num.append(num2*num1)
                else:
                    stack_num.append(int(num2/num1))


        return stack_num[-1]
