class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results = [''] * n

        for i in range(1, n + 1):
            if i % 3 == 0: results[i - 1] += "Fizz"
            if i % 5 == 0: results[i - 1] += "Buzz"
            if results[i - 1] == '': results[i - 1] = str(i)

        return results
