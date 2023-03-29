import itertools
class Solution(object):
    def countAndSay(sel, n):
        """
        input : int n
        :return: string
        """
        result = '1'
        for i in range(n-1):
            additional = ''
            for digit, group in itertools.groupby(result):
                count = len(list(group))
                additional += '%i%s'%(count,digit)
            result = additional
        return result
    def countAndSay2(self, n):
        """
                input : int n
                :return: string
                """
        result = '1'
        for i in range(n - 1):
            additional = ''
            j = 0
            while j < len(result):
                count = 1
                digit = result[j]
                while j+1 < len(result) and result[j] == result[j+1]:
                    count +=1
                    j +=1
                additional += '%i%s' % (count, digit)
                j +=1
            result = additional
        return result



# time complexity O(N^2)
# space complexity O(N)

print("method 1 itertool")
print (Solution().countAndSay(5))
print (Solution().countAndSay(1))
print (Solution().countAndSay(0))
print (Solution().countAndSay(2))
print (Solution().countAndSay(3))
print("method 2 while loop")
print (Solution().countAndSay2(5))
print (Solution().countAndSay2(1))
print (Solution().countAndSay2(0))
print (Solution().countAndSay2(2))
print (Solution().countAndSay2(3))

