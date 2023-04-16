# 242. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid. The brackets must close in the correct order.

class Solution(object):
    def validParentheses(self,strs):
        '''
        :param str: String
        :return: boolean
        '''
        if not strs:
            return True
        if len(strs)%2 ==1:
            return False
        tmp = []
        dict = {'(':')', '{':'}','[':']'}
        for i in range(len(strs)):
            if strs[i] in dict:
                tmp.append(dict[strs[i]])
            # need to check whether the tmp is valid
            elif tmp and strs[i] == tmp[-1]:
                tmp.pop()
            else:
                return False
        return len(tmp) == 0

# time complexity O(n)
# space complexity O(n)

test1 = "[][][][][][]{}()()(){}"
test2 = "[()]{}{}[(]"
test3 = ""
test4 = "]"

print(Solution().validParentheses(test1))
print(Solution().validParentheses(test2))
print(Solution().validParentheses(test3))
print(Solution().validParentheses(test4))



