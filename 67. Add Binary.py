"""
class Solution:
    def addBinary(self, a: str, b: str):
        af = a[::-1]
        bf = b[::-1]
        if len(a)>len(b):
            t =len(b)
            m =a[0:len(a)-len(b)]
        else:
            t =len(a)
            m =b[0:len(b)-len(a)]
        for i in range(t):
            n = int

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, plus = len(a)-1, len(b)-1, 0
        while (plus==1) or (i>=0 or j>=0):
            #print("plus1:%d" % plus)
            plus += int(a[i]) if i>= 0 else 0
            plus += int(b[j]) if j>= 0 else 0        
            print("plus2:%d" % plus)
            res = str(int(plus % 2))+res
            #print("plus2:%d" % plus)
            print(res)
            i, j, plus = i-1, j-1, plus//2
            #print("plus3:%d" % plus)
        return res

test1 = Solution().addBinary("1010","1011")
print(test1)