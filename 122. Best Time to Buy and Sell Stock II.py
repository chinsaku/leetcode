class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)<=0):
            return 0
        all_profit = 0
        m = 0
        #n = m
        while m < len(prices):
            max_profit = 0
            min_num = prices[m]
            for i in range(m,len(prices)):
                min_num=min(min_num,prices[i])
                if prices[i]> min_num:
                    max_profit += prices[i] - min_num
                    all_profit += max_profit
                    m = i 
                    break
                m = m +1
        return all_profit

a = Solution().maxProfit([7,1,5,3,6,4])
print(a)