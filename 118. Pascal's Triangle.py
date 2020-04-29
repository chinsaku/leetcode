class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        queue = [[1],[1,1]]
        for i in range(2,numRows):
            lines=[1,1]
            for m in range(1,i):
                lines.insert(m,queue[i-1][m-1]+queue[i-1][m])
                #print('lines=',lines)
            queue.append(lines)
            #print('queue=',queue)
        return queue


a = Solution().generate(4)
print(a)