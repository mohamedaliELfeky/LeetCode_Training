class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        counter = 0
        temp = ""
        a, b = (str1, str2) if len(str1) > len(str2) else (str2, str1)

        for i in range(len(b)):

            base_str = b[:i + 1]

            a_len, b_len, base_len = len(a), len(b), len(base_str)
            div = b_len % base_len

            if not div and base_str * int(b_len / base_len) == b:

                if not (a_len % base_len) and base_str * int(a_len / base_len) == a:
                    if len(base_str) > counter:
                        counter = len(base_str)
                        temp = base_str

        return temp
    

