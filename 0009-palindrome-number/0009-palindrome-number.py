class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        index = -1
        for el in x:
            if el != x[index]:
                return False
            index -= 1
        return True