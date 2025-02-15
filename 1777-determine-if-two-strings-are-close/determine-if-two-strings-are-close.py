class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        c1 = Counter(word1)
        c2 = Counter(word2)

        f1 = Counter([f for f in c1.values()])
        f2 = Counter([f for f in c2.values()])

        return c1 ==  c2 or (f1 == f2 and set(word1) == set(word2))