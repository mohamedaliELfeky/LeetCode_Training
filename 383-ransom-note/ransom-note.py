class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = dict()
        for char in magazine:
            mag_dict[char] = mag_dict.get(char, 0) + 1

        for char in ransomNote:
            if mag_dict.get(char, 0):
                mag_dict[char] -= 1
            else:
                return False

        return True