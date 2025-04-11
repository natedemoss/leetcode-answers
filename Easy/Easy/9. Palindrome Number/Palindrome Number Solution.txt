class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reversed_x = x[::-1]
        if reversed_x == x:
            return True
        elif reversed_x != x:
            return False
