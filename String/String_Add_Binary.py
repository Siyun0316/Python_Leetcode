# Add Binary
# Given two binary strings, return their sum (also a binary string).
# Input: a = “11”
#        b = “1”
# Output: “100”
import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        input: string a, string b
        return: string
        """
        if not a:
            return b
        if not b:
            return a
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        res = []
        while i >= 0 or j >= 0:
            res_tmp = carry
            if i >= 0:
                res_tmp += int(a[i])
                i -= 1
            if j >= 0:
                res_tmp += int(b[j])
                j -= 1
            carry = res_tmp // 2
            res.append(str(res_tmp % 2))
        if carry == 1:
            res.append(str(carry))
        return ''.join(res[::-1])

class Test(unittest.TestCase):
    def test_addBinary(self):
        solu = Solution()

        _inp1 = '11'
        _inp2 = '1'
        _out = '100'
        self.assertEqual(solu.addBinary(_inp1,_inp2), _out)

        _inp1 = "1010101010"
        _inp2 = "10101010"
        _out = "1101010100"
        self.assertEqual(solu.addBinary(_inp1, _inp2), _out)

        _inp1 = ""
        _inp2 = "10101010"
        _out = "10101010"
        self.assertEqual(solu.addBinary(_inp1, _inp2), _out)


