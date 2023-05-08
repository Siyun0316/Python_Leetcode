# All Permutations I
# Given a string with no duplicate characters, return a list with all permutations of the characters.
# Assume that input string is not null.
# Examples
# Set = “abc”, all permutations are [“abc”, “acb”, “bac”, “bca”, “cab”, “cba”]
# Set = "", all permutations are [""]

class Solution(object):
    def permutations(self, input):
        """
        input: string input
        return: string[]
        """
        if not input:
            return [""]
        if len(input) == 1:
            return [input]
        res = []
        self.dfs(list(input), 0, res)
        return sorted(res)

    def dfs(self, inp, index, res):
        if index == len(inp)-1 :
            return res.append(''.join(inp))
        for i in range(index, len(inp)):
            inp[i], inp[index] = inp[index], inp[i]
            self.dfs(inp, index+1, res)
            inp[i], inp[index] = inp[index], inp[i]
        return res

# time complexity O(n*n!)
# space complexity O(n)

s = Solution()

# Test case 1: empty input
assert s.permutations("") == [""]

# Test case 2: single character input
assert s.permutations("a") == ["a"]

# Test case 3: two-character input
assert s.permutations("ab") == ["ab", "ba"]

# Test case 4: three-character input
assert s.permutations("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]

# Test case 5: input with spaces
assert s.permutations("bcijm") == ["bcijm", "bcimj", "bcjim", "bcjmi", "bcmij", "bcmji", "bicjm", "bicmj", "bijcm", "bijmc", "bimcj", "bimjc", "bjcim", "bjcmi", "bjicm", "bjimc", "bjmci", "bjmic", "bmcij", "bmcji", "bmicj", "bmijc", "bmjci", "bmjic", "cbijm", "cbimj", "cbjim", "cbjmi", "cbmij", "cbmji", "cibjm", "cibmj", "cijbm", "cijmb", "cimbj", "cimjb", "cjbim", "cjbmi", "cjibm", "cjimb", "cjmbi", "cjmib", "cmbij", "cmbji", "cmibj", "cmijb", "cmjbi", "cmjib", "ibcjm", "ibcmj", "ibjcm", "ibjmc", "ibmcj", "ibmjc", "icbjm", "icbmj", "icjbm", "icjmb", "icmbj", "icmjb", "ijbcm", "ijbmc", "ijcbm", "ijcmb", "ijmbc", "ijmcb", "imbcj", "imbjc", "imcbj", "imcjb", "imjbc", "imjcb", "jbcim", "jbcmi", "jbicm", "jbimc", "jbmci", "jbmic", "jcbim", "jcbmi", "jcibm", "jcimb", "jcmbi", "jcmib", "jibcm", "jibmc", "jicbm", "jicmb", "jimbc", "jimcb", "jmbci", "jmbic", "jmcbi", "jmcib", "jmibc", "jmicb", "mbcij", "mbcji", "mbicj", "mbijc", "mbjci", "mbjic", "mcbij", "mcbji", "mcibj", "mcijb", "mcjbi", "mcjib", "mibcj", "mibjc", "micbj", "micjb", "mijbc", "mijcb", "mjbci", "mjbic", "mjcbi", "mjcib", "mjibc", "mjicb"]

