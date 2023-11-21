class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        new_str = []
        
        for i in range(min(len(word1), len(word2))):
            new_str.append(word1[i])
            new_str.append(word2[i])


        if len(word1) != len(word2):
            a, b = (word1, word2) if len(word1) > len(word2) else (word2, word1)

            new_str += list(a[len(b):])


        return ''.join(new_str)

        