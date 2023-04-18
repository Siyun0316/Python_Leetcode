# Reverse Words In A Sentence II
# Reverse the words in a sentence and truncate all heading/trailing/duplicate space characters.
# Examples
# “ I  love  Google  ” → “Google love I”
# Corner Cases
# If the given string is null, we do not need to do anything.

import unittest

class Solution(object):
    def reverseWords(self, input):
        """
        input: string input
        return: string
        """
        if not input or len(input)<2:
            return input
        tmp = ''
        reversed_res_list = []
        i = 0
        while i < len(input):
            if input[i].isalpha():
                while input[i].isalpha():
                    tmp = tmp + input[i]
                    i += 1
            while i == len(input) - 1 or (i < len(input) and not input[i].isalpha()):
                if tmp != '':
                    reversed_res_list.append(tmp)
                    tmp = ''
                i+=1
        return ' '.join(reversed_res_list[::-1])

# time complexity O(n)
# space complexity O(n)

# inplace method  reverse twice
    def reverseWords2(self, input):
        """
        input: string input
        return: string
        """
        if not input or len(input) < 2:
            return input
        inp = list(input)
        end = 0
        for i in range(len(input)):
            if inp[i] == " " and (i == 0 or inp[i-1] == " "):
                continue
            inp[end] = inp[i]
            end += 1
        if end > 0 and inp[end-1] == " ":
            end -= 1
        self.reverse(inp, 0, end-1)
        st_word, end_word = 0, 0
        i = 0
        while i < end:
            if inp[i].isalpha():
                st_word = i
                while inp[i].isalpha():
                    end_word = i
                    i += 1
            else:
                self.reverse(inp, st_word, end_word)
                i += 1
        return ''.join(inp[:end])

    def reverse(self, array, l, r):
        while l < r:
            array[l], array[r] = array[r], array[l]
            l += 1
            r -= 1
        return

# time complexity O(4n)
# space complexity O(1)


class Test(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()

        input = "I  love  Google  "
        output = "Google love I"
        self.assertEqual(solution.reverseWords(input), output)
        self.assertEqual(solution.reverseWords2(input), output)

        input = " A B C D "
        output = "D C B A"
        self.assertEqual(solution.reverseWords(input), output)
        self.assertEqual(solution.reverseWords2(input), output)

        input = " A   B   C  D "
        output = "D C B A"
        self.assertEqual(solution.reverseWords(input), output)
        self.assertEqual(solution.reverseWords2(input), output)

        input = "     "
        output = ""
        self.assertEqual(solution.reverseWords(input), output)
        self.assertEqual(solution.reverseWords2(input), output)


