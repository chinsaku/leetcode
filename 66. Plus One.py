class Solution:
    def plusOne(self,digits):
        m =[str(i) for i in digits]
        a =''.join(m)
        b = int(a)
        c = b+1
        d = str(c)
        #e =d.split('')
        return list(d)


c = Solution().plusOne([9,9,9])
print(c)