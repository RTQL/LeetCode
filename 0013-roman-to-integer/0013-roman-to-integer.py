class Solution:
    def romanToInt(self, s: str) -> int:
        integer = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        for index, symbol in enumerate(s[:-1]):
            value = roman[symbol]
            if roman[s[index + 1]] <= value:
                integer += value
            else:
                integer -= value
        integer += roman[s[-1]]
        return integer