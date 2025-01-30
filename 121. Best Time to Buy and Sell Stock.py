from typing import List
class Solve:
    def maxProfit(self,prices:List[int])->int:
        maxProfit=0
        bestbuy=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>bestbuy:
                maxProfit=max(maxProfit,prices[i]-bestbuy)

            bestbuy=min(maxProfit,prices[i])
            
        return maxProfit




    
