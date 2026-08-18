class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sqsum(num):
            sum = 0
            
            while num > 0:
                r = num % 10
                sum = sum + r * r
                num = num // 10
            return sum
        
        seen = set()
        while sqsum(n) != 1:
            sum1 = sqsum(n)
            if sum1 == 1:
                return True
            else:
                seen.add(sum1)
                n = sum1
        return False
        
        