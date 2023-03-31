# Number of Matching Subsequences
# Given a string s and an array of strings words,
# return the number of words[i] that is a subsequence of s.
# A subsequence of a string is a new string generated from
# the original string with some characters (can be none) deleted without
# changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

from collections import defaultdict
class Solution(object):
    def numOfMatchSubseq(self,s, words):
        '''
        :param s string:
        :param words List[str]:
        :return int:
        '''
        tmp_dic = defaultdict(list)
        count = 0
        for x in words:
            tmp_dic[x[0]].append(x)
        for char in s:
            for w in tmp_dic.pop(char):
                if len(w) ==1:
                    count +=1
                else:
                    tmp_dic[w[1]].append(w[1:])
        return count
# time complexity O(m*n) m is length of s and n is length of words
# space complexity O(n)
#test
s1 = 'sdfdafd'
words1 = ['s','sdfd','sdf','ad','af']
print(Solution().numOfMatchSubseq(s1,words1))



