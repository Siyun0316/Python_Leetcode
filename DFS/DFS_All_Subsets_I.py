# All Subsets I
# Given a set of characters represented by a String, return a list containing all subsets of the characters.
# Assumptions
# There are no duplicate characters in the original set.
# Examples
# Set = "abc", all the subsets are [“”, “a”, “ab”, “abc”, “ac”, “b”, “bc”, “c”]
# Set = "", all the subsets are [""]
# Set = null, all the subsets are

class Solution(object):
    def subSets(self, set):
        """
        input : String set
        return : String[]
        """
        if not set:
            return []
        res = []
        tmp = []
        self.dfs(set, res, tmp, 0)
        return res

    def dfs(self, set, res, tmp, idx):
        if idx == len(set):
            res.append(''.join(tmp))
            return
        # abc, a
        self.dfs(set, res, tmp, idx+1)
        tmp.append(set[idx])
        self.dfs(set, res, tmp, idx+1)
        tmp.pop()
        return

    def subSets2(self, set):
        """
        input : String set
        return : String[]
        """
        if not set:
            return []
        res = []
        tmp = []
        self.dfs2(set, res, tmp, 0)
        return res

    def dfs2(self, set, res, tmp, idx):
        if idx < len(set):
            for i in range(idx, len(set)):
                self.dfs2(set, res, tmp + [set[i]], i+1)
        res.append(''.join(tmp))


# time complexity O(2^n)
# space complexity O(n)

print (Solution().subSets('abc'))
print (Solution().subSets2('abc'))


print (Solution().subSets(''))
print (Solution().subSets2(''))

print (Solution().subSets('ed'))
print (Solution().subSets2('ed'))