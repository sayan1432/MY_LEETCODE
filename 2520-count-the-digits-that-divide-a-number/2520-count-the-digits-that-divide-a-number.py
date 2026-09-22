class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        ori = num
        while num > 0:
            val = num % 10
            if val != 0 and ori % val == 0:
                count += 1
            num //= 10
        return count
             
             

