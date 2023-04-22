# Reverse Words In A Sentence I
# Reverse the words in a sentence.
# Assumptions
#       Words are separated by single space
#       There are no heading or tailing white spaces
# Examples
#       “I love Google” → “Google love I”
# Corner Cases
#       If the given string is null, we do not need to do anything.

import unittest


class Solution(object):
    def reverseWords(self, input):
        '''
        :param input: string
        :return: string
        '''
        if len(input)<2:
            return input
        res = []
        tmp = ''
        for i in range(len(input)):
            if input[i].isalpha():
                tmp = tmp + str(input[i])
            else:
                res.append(tmp)
                tmp = ''
        res.append(tmp)
        return ' '.join(res[::-1])

# time complexity O(n)
# space complexity O(1)

class Test(unittest.TestCase):
    def test_reverse(self):
        _input = "I love Google"
        _output = "Google love I"
        self.assertEqual(Solution().reverseWords(_input), _output)

        _input = 'Ilove Google'
        _output = 'Google Ilove'
        self.assertEqual(Solution().reverseWords(_input), _output)