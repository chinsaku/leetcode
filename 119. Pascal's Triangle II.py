class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        a = self.getRow(rowIndex-1)
        b = [1,1]
        for m in range(1,rowIndex):
            b.insert(m,a[m-1]+a[m])
        return b

t = Solution().getRow(4)
print(t)