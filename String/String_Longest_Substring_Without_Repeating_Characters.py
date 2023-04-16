# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        if len(s)<2:
            return len(s)
        max_len = 0
        st,end = 0,0
        helper_set = set()
        while end < len(s):
            if s[end] not in helper_set:
                helper_set.add(s[end])
                end +=1
                max_len = max(max_len, len(helper_set))
            else:
                helper_set.remove(s[st])
                st +=1
        return max_len

# time complexity O(n)
# space complexity O(k) k = max_len

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(Solution().lengthOfLongestSubstring(s1))
print(Solution().lengthOfLongestSubstring(s2))
print(Solution().lengthOfLongestSubstring(s3))