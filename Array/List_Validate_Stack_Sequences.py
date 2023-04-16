# 615. Validate Stack Sequences
# Given two sequences pushed and popped with distinct values,
# return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

class Solution(object):
    def validateStackSequences(self,pushed,popped):
        """
        input: int[] pushed, int[] popped
        return: boolean
        """
        if len(pushed) != len(popped):
            return False
        if not pushed and not popped:
            return True
        tmp = []
        i,j = 0,0
        while i < len(pushed) and j<len(popped):
            tmp.append(pushed[i])
            i += 1
            while len(tmp)>0 and tmp[-1] == popped[j]:
                tmp.pop()
                j += 1
        return len(tmp) == 0

    def validateStackSequences2(self,pushed,popped):
        """
        input: int[] pushed, int[] popped
        return: boolean
        """
        tmp = []
        j = 0
        for x in pushed:
            tmp.append(x)
            while len(tmp)>0 and tmp[-1] == popped[j]:
                tmp.pop()
                j += 1
        return len(tmp) == 0

    def validateStackSequences3(self,pushed,popped):
        """
        input: int[] pushed, int[] popped
        return: boolean
        """
        tmp = []
        j = 0
        for x in popped:
            while (not tmp or tmp[-1] != x) and j < len(pushed):
                tmp.append(pushed[j])
                j += 1
            if tmp[-1] != x:
                break
            tmp.pop()
        return len(tmp) == 0

# time complexity O(n)
# space complexity O(n)

pushed1 = [1,2,3,4,5]
popped1 = [4,5,3,2,1]
pushed2 = [1,2,3,4,5]
popped2 = [4,3,5,1,2]

print(Solution().validateStackSequences(pushed1,popped1))
print(Solution().validateStackSequences(pushed2,popped2))

print(Solution().validateStackSequences2(pushed1,popped1))
print(Solution().validateStackSequences2(pushed2,popped2))

print(Solution().validateStackSequences3(pushed1,popped1))
print(Solution().validateStackSequences3(pushed2,popped2))

