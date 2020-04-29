"""
class Solution:
    def maxProfit(self, prices):
        if prices ==[]:
            return 0
        output = 0
        
        queue = prices[::-1]
        for i in range(0,len(queue)):
            if queue[i] <= output:
                #print(queue[i])
                #print(output)
                continue
            m = max([queue[i]- p for p in queue[i:]])
            #print('m=',m)
            if m > output:
                output =m
        return output
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
 
 
        if(len(prices)<=0):
            return 0
        min_num=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            min_num=min(min_num,prices[i])
            max_profit=max(max_profit,prices[i]-min_num)
        return max_profit

x =Solution().maxProfit([3,2,6,5,0,3])
print(x)