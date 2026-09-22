class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        s = x
        while s>0:
            a = a*10 + (s%10)
            s = s // 10
            #rev += 1
        if (a == x):
            return True
        else:
            return False
            