class Solution:
    def maxProfit(self, price: List[int]) -> int:
        left = 0  #left pointer = buy
        right = 1 #right pointer = sell
        maxP = 0 
        
        while right < len(price):
            #profitable?
            if price[left] < price[right]:
                profit = price[right] - price[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
            
        return maxP