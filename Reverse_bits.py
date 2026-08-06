class solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        if n == 0:
            return 0
        
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
    
    