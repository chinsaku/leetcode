class Solution:
    def isValid(self, s: str) -> bool:
        dictstr = {'(': 1, '{': 2, '[': 3, ')': -1, '}': -2, ']': -3}
        num = int(len(s) / 2)
        
        if len(s) % 2 != 0:
            return False
        else:
            for i in range(num):
                m = 0
                while m < len(s):
                    #print('m1={0}'.format(m))
                    #print('len={0}'.format(len(s)))
                    if (dictstr[s[0]] + (dictstr[s[m]])) == 0:
                        s = s[1:]
                        s = s[:m - 1] + s[m:]
                    #print(s[m])
                    #print('m2={0}'.format(m))
                    m +=1
                    #print(s)
                    # print(i)
                #print('i={0}'.format(i))
                        
        if s == "":
            return True
        else:
            return False


try1 = Solution().isValid(s="()")
print(try1)




"""
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True

for x in range(len(s))
这个 x 在一开始的时候是固定的，
不随len(s)变化而变化
"""