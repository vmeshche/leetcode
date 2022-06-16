"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""

class Solution:

    def romanToInt(self, s: str) -> int:

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                num += roman[s[i]] - 2 * roman[s[i - 1]]
            else:
                num += roman[s[i]]
        return num



if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt("MCMVIII"))