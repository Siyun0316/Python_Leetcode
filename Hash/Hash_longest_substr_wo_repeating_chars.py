#Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        '''
        :param s:
        :return int:
        '''
        st_i,max_c = 0,0
        tmp_h = {}
        for i in range(len(s)):
            tmp_h[s[i]] = tmp_h.get(s[i],0)+1
            while tmp_h[s[i]]>1:
                tmp_h[s[st_i]] -=1
                st_i +=1
            max_c = max(max_c,i-st_i+1)
        return max_c

#time complexity O(n)
#space complexity O(n)

test1 = "asdfgfgggsdssdfdsa"
test2 = "asdfghjkasdfdfdg"
test3 = "aaaaaaaabbbbbbcccccc"
test4 = ""
print(Solution().lengthOfLongestSubstring(test1))
print(Solution().lengthOfLongestSubstring(test2))
print(Solution().lengthOfLongestSubstring(test3))
print(Solution().lengthOfLongestSubstring(test4))
