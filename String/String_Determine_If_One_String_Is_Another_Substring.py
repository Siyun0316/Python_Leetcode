# Determine If One String Is Another's Substring
# Determine if a small string is a substring of another large string.
# Return the index of the first occurrence of the small string in the large string.
# Return -1 if the small string is not a substring of the large string.
# Assumptions
# Both large and small are not null
# If small is empty string, return 0
# Examples
# “ab” is a substring of “bcabc”, return 2
# “bcd” is not a substring of “bcabc”, return -1
# "" is substring of "abc", return 0


class Solution(object):
    def strstr(self, large, small):
        """
        input: string large, string small
        return: int
        """
        # write your solution here
        if not small:
            return 0
        if not large:
            return -1
        l, r = 0, len(large ) -1
        st = 0
        while l< r:
            if large[l] != small[0]:
                l += 1
            elif large[r] != small[-1]:
                r -= 1
            elif r - l + 1 < len(small):
                return -1
            else:
                st = l
                i = 0
                while i < len(small) and l <= r and large[l] == small[i]:
                    l += 1
                    i += 1
                if i == len(small):
                    return st
                else:
                    l = st + 1
        return -1

# time complexity O(n+m)
# space complexity O(1)



solution = Solution()

# Test Case 1
assert solution.strstr("hello", "ll") == 2

# Test Case 2
assert solution.strstr("world", "abc") == -1

# Test Case 3
assert solution.strstr("", "a") == -1

# Test Case 4
assert solution.strstr("ababcabcacbab", "abcac") == 5

# Test Case 5
assert solution.strstr("aaaaa", "aa") == 0

# Test Case 6
assert solution.strstr("ababababac", "ababaca") == -1

# Test Case 7
assert solution.strstr("ababababac", "abababac") == 2





