# 8. Evaluate Reverse Polish Notation
#  Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Assumption
# Valid operators are +, -, *, /.
# Each operand may be an integer or another expression.

import operator
class Solution(object):
    def evalRPN(self,tokens):
        '''
        :param tokens: list[string]
        :return: int
        '''
        if not tokens:
            return -1
        opr_dict = {'+':operator.add, '-':operator.sub, '/':operator.truediv, '*':operator.mul}
        function = []
        for x in tokens:
            if x not in opr_dict:
                function.append(int(x))
            else:
                b,a = function.pop(),function.pop()
                function.append(int(opr_dict[x](a,b)))
        return function[-1]

# time complexity O(n)
# space complexity O(n)

test1 = ["0","12","4","+","-"]
test2 = ["2", "1", "+", "3", "*"]
test3 = ["4", "13", "5", "/", "+"]
print(Solution().evalRPN(test1))
print(Solution().evalRPN(test2))
print(Solution().evalRPN(test3))