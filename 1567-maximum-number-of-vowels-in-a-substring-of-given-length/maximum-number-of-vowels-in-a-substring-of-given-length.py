class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set('aouei')

        n = len(s)
        if n == k:
            return self.get_vowels_num(s)

        
        max_num = self.get_vowels_num(s[:k])
        crrn = max_num
        for i in range(1, n - k + 1):

            left = s[i - 1] in vowels
            right = s[i + k - 1] in vowels

            crrn -= left
            crrn += right

            max_num = max(max_num, crrn)

        return max_num


    def get_vowels_num(self, sub_s:str):

        vowels = set('aouei')
        
        return sum(1 for s in sub_s if s in vowels)

        






        
