# All Permutations II
# Given a string with possible duplicate characters, return a list with all permutations of the characters.
# Examples
# Set = “abc”, all permutations are [“abc”, “acb”, “bac”, “bca”, “cab”, “cba”]
# Set = "aba", all permutations are ["aab", "aba", "baa"]
# Set = "", all permutations are [""]
# Set = null, all permutations are []

class Solution(object):
    def permutations(self, input):
        """
        input: string input
        return: string[]
        """
        if len(input) == 0:
            return [""]
        res = []
        inp = list(input)
        def dfs(idx):
            if idx == len(input):
                res.append(''.join(inp))
                return
            _exist = set()
            for i in range(idx, len(inp)):
                if inp[i] in _exist:
                    continue
                _exist.add(inp[i])
                inp[i], inp[idx] = inp[idx], inp[i]
                dfs(idx+1)
                inp[i], inp[idx] = inp[idx], inp[i]
            return
        dfs(0)
        return sorted(res) # sort for tests

# time complexity O(n!)
# space complexity O(n^2)

assert Solution().permutations('abcadcd') == ["aabccdd", "aabcdcd", "aabcddc", "aabdccd", "aabdcdc", "aabddcc", "aacbcdd", "aacbdcd", "aacbddc", "aaccbdd", "aaccdbd", "aaccddb", "aacdbcd", "aacdbdc", "aacdcbd", "aacdcdb", "aacddbc", "aacddcb", "aadbccd", "aadbcdc", "aadbdcc", "aadcbcd", "aadcbdc", "aadccbd", "aadccdb", "aadcdbc", "aadcdcb", "aaddbcc", "aaddcbc", "aaddccb", "abaccdd", "abacdcd", "abacddc", "abadccd", "abadcdc", "abaddcc", "abcacdd", "abcadcd", "abcaddc", "abccadd", "abccdad", "abccdda", "abcdacd", "abcdadc", "abcdcad", "abcdcda", "abcddac", "abcddca", "abdaccd", "abdacdc", "abdadcc", "abdcacd", "abdcadc", "abdccad", "abdccda", "abdcdac", "abdcdca", "abddacc", "abddcac", "abddcca", "acabcdd", "acabdcd", "acabddc", "acacbdd", "acacdbd", "acacddb", "acadbcd", "acadbdc", "acadcbd", "acadcdb", "acaddbc", "acaddcb", "acbacdd", "acbadcd", "acbaddc", "acbcadd", "acbcdad", "acbcdda", "acbdacd", "acbdadc", "acbdcad", "acbdcda", "acbddac", "acbddca", "accabdd", "accadbd", "accaddb", "accbadd", "accbdad", "accbdda", "accdabd", "accdadb", "accdbad", "accdbda", "accddab", "accddba", "acdabcd", "acdabdc", "acdacbd", "acdacdb", "acdadbc", "acdadcb", "acdbacd", "acdbadc", "acdbcad", "acdbcda", "acdbdac", "acdbdca", "acdcabd", "acdcadb", "acdcbad", "acdcbda", "acdcdab", "acdcdba", "acddabc", "acddacb", "acddbac", "acddbca", "acddcab", "acddcba", "adabccd", "adabcdc", "adabdcc", "adacbcd", "adacbdc", "adaccbd", "adaccdb", "adacdbc", "adacdcb", "adadbcc", "adadcbc", "adadccb", "adbaccd", "adbacdc", "adbadcc", "adbcacd", "adbcadc", "adbccad", "adbccda", "adbcdac", "adbcdca", "adbdacc", "adbdcac", "adbdcca", "adcabcd", "adcabdc", "adcacbd", "adcacdb", "adcadbc", "adcadcb", "adcbacd", "adcbadc", "adcbcad", "adcbcda", "adcbdac", "adcbdca", "adccabd", "adccadb", "adccbad", "adccbda", "adccdab", "adccdba", "adcdabc", "adcdacb", "adcdbac", "adcdbca", "adcdcab", "adcdcba", "addabcc", "addacbc", "addaccb", "addbacc", "addbcac", "addbcca", "addcabc", "addcacb", "addcbac", "addcbca", "addccab", "addccba", "baaccdd", "baacdcd", "baacddc", "baadccd", "baadcdc", "baaddcc", "bacacdd", "bacadcd", "bacaddc", "baccadd", "baccdad", "baccdda", "bacdacd", "bacdadc", "bacdcad", "bacdcda", "bacddac", "bacddca", "badaccd", "badacdc", "badadcc", "badcacd", "badcadc", "badccad", "badccda", "badcdac", "badcdca", "baddacc", "baddcac", "baddcca", "bcaacdd", "bcaadcd", "bcaaddc", "bcacadd", "bcacdad", "bcacdda", "bcadacd", "bcadadc", "bcadcad", "bcadcda", "bcaddac", "bcaddca", "bccaadd", "bccadad", "bccadda", "bccdaad", "bccdada", "bccddaa", "bcdaacd", "bcdaadc", "bcdacad", "bcdacda", "bcdadac", "bcdadca", "bcdcaad", "bcdcada", "bcdcdaa", "bcddaac", "bcddaca", "bcddcaa", "bdaaccd", "bdaacdc", "bdaadcc", "bdacacd", "bdacadc", "bdaccad", "bdaccda", "bdacdac", "bdacdca", "bdadacc", "bdadcac", "bdadcca", "bdcaacd", "bdcaadc", "bdcacad", "bdcacda", "bdcadac", "bdcadca", "bdccaad", "bdccada", "bdccdaa", "bdcdaac", "bdcdaca", "bdcdcaa", "bddaacc", "bddacac", "bddacca", "bddcaac", "bddcaca", "bddccaa", "caabcdd", "caabdcd", "caabddc", "caacbdd", "caacdbd", "caacddb", "caadbcd", "caadbdc", "caadcbd", "caadcdb", "caaddbc", "caaddcb", "cabacdd", "cabadcd", "cabaddc", "cabcadd", "cabcdad", "cabcdda", "cabdacd", "cabdadc", "cabdcad", "cabdcda", "cabddac", "cabddca", "cacabdd", "cacadbd", "cacaddb", "cacbadd", "cacbdad", "cacbdda", "cacdabd", "cacdadb", "cacdbad", "cacdbda", "cacddab", "cacddba", "cadabcd", "cadabdc", "cadacbd", "cadacdb", "cadadbc", "cadadcb", "cadbacd", "cadbadc", "cadbcad", "cadbcda", "cadbdac", "cadbdca", "cadcabd", "cadcadb", "cadcbad", "cadcbda", "cadcdab", "cadcdba", "caddabc", "caddacb", "caddbac", "caddbca", "caddcab", "caddcba", "cbaacdd", "cbaadcd", "cbaaddc", "cbacadd", "cbacdad", "cbacdda", "cbadacd", "cbadadc", "cbadcad", "cbadcda", "cbaddac", "cbaddca", "cbcaadd", "cbcadad", "cbcadda", "cbcdaad", "cbcdada", "cbcddaa", "cbdaacd", "cbdaadc", "cbdacad", "cbdacda", "cbdadac", "cbdadca", "cbdcaad", "cbdcada", "cbdcdaa", "cbddaac", "cbddaca", "cbddcaa", "ccaabdd", "ccaadbd", "ccaaddb", "ccabadd", "ccabdad", "ccabdda", "ccadabd", "ccadadb", "ccadbad", "ccadbda", "ccaddab", "ccaddba", "ccbaadd", "ccbadad", "ccbadda", "ccbdaad", "ccbdada", "ccbddaa", "ccdaabd", "ccdaadb", "ccdabad", "ccdabda", "ccdadab", "ccdadba", "ccdbaad", "ccdbada", "ccdbdaa", "ccddaab", "ccddaba", "ccddbaa", "cdaabcd", "cdaabdc", "cdaacbd", "cdaacdb", "cdaadbc", "cdaadcb", "cdabacd", "cdabadc", "cdabcad", "cdabcda", "cdabdac", "cdabdca", "cdacabd", "cdacadb", "cdacbad", "cdacbda", "cdacdab", "cdacdba", "cdadabc", "cdadacb", "cdadbac", "cdadbca", "cdadcab", "cdadcba", "cdbaacd", "cdbaadc", "cdbacad", "cdbacda", "cdbadac", "cdbadca", "cdbcaad", "cdbcada", "cdbcdaa", "cdbdaac", "cdbdaca", "cdbdcaa", "cdcaabd", "cdcaadb", "cdcabad", "cdcabda", "cdcadab", "cdcadba", "cdcbaad", "cdcbada", "cdcbdaa", "cdcdaab", "cdcdaba", "cdcdbaa", "cddaabc", "cddaacb", "cddabac", "cddabca", "cddacab", "cddacba", "cddbaac", "cddbaca", "cddbcaa", "cddcaab", "cddcaba", "cddcbaa", "daabccd", "daabcdc", "daabdcc", "daacbcd", "daacbdc", "daaccbd", "daaccdb", "daacdbc", "daacdcb", "daadbcc", "daadcbc", "daadccb", "dabaccd", "dabacdc", "dabadcc", "dabcacd", "dabcadc", "dabccad", "dabccda", "dabcdac", "dabcdca", "dabdacc", "dabdcac", "dabdcca", "dacabcd", "dacabdc", "dacacbd", "dacacdb", "dacadbc", "dacadcb", "dacbacd", "dacbadc", "dacbcad", "dacbcda", "dacbdac", "dacbdca", "daccabd", "daccadb", "daccbad", "daccbda", "daccdab", "daccdba", "dacdabc", "dacdacb", "dacdbac", "dacdbca", "dacdcab", "dacdcba", "dadabcc", "dadacbc", "dadaccb", "dadbacc", "dadbcac", "dadbcca", "dadcabc", "dadcacb", "dadcbac", "dadcbca", "dadccab", "dadccba", "dbaaccd", "dbaacdc", "dbaadcc", "dbacacd", "dbacadc", "dbaccad", "dbaccda", "dbacdac", "dbacdca", "dbadacc", "dbadcac", "dbadcca", "dbcaacd", "dbcaadc", "dbcacad", "dbcacda", "dbcadac", "dbcadca", "dbccaad", "dbccada", "dbccdaa", "dbcdaac", "dbcdaca", "dbcdcaa", "dbdaacc", "dbdacac", "dbdacca", "dbdcaac", "dbdcaca", "dbdccaa", "dcaabcd", "dcaabdc", "dcaacbd", "dcaacdb", "dcaadbc", "dcaadcb", "dcabacd", "dcabadc", "dcabcad", "dcabcda", "dcabdac", "dcabdca", "dcacabd", "dcacadb", "dcacbad", "dcacbda", "dcacdab", "dcacdba", "dcadabc", "dcadacb", "dcadbac", "dcadbca", "dcadcab", "dcadcba", "dcbaacd", "dcbaadc", "dcbacad", "dcbacda", "dcbadac", "dcbadca", "dcbcaad", "dcbcada", "dcbcdaa", "dcbdaac", "dcbdaca", "dcbdcaa", "dccaabd", "dccaadb", "dccabad", "dccabda", "dccadab", "dccadba", "dccbaad", "dccbada", "dccbdaa", "dccdaab", "dccdaba", "dccdbaa", "dcdaabc", "dcdaacb", "dcdabac", "dcdabca", "dcdacab", "dcdacba", "dcdbaac", "dcdbaca", "dcdbcaa", "dcdcaab", "dcdcaba", "dcdcbaa", "ddaabcc", "ddaacbc", "ddaaccb", "ddabacc", "ddabcac", "ddabcca", "ddacabc", "ddacacb", "ddacbac", "ddacbca", "ddaccab", "ddaccba", "ddbaacc", "ddbacac", "ddbacca", "ddbcaac", "ddbcaca", "ddbccaa", "ddcaabc", "ddcaacb", "ddcabac", "ddcabca", "ddcacab", "ddcacba", "ddcbaac", "ddcbaca", "ddcbcaa", "ddccaab", "ddccaba", "ddccbaa"]
assert Solution().permutations('abc') == ["abc", "acb", "bac", "bca", "cab", "cba"]
assert Solution().permutations('') == [""]
