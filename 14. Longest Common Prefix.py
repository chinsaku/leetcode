class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if  len(strs) == 0: return ""
        alpha = []
        strlast = ""
        num = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < num:
                num = len(strs[i])
        # print(num)
        for i in range(num):
            sum = 0
            for m in range(len(strs)):
                if strs[0][i] == strs[m][i]:
                    sum += 1
                    # print('sum={0},m={1}'.format(sum,m))
                    if sum == len(strs):
                        alpha.append(strs[0][i])
                else:
                    return strlast.join(alpha)
                    
                

        return strlast.join(alpha)


try1 = Solution().longestCommonPrefix(strs=["aca","cba"])
print(try1)

class Solution2:
    def longestCommonPrefix(self, strs):
        if  len(strs) == 0: return ""
        c = 0
        for i in range(len(strs[0])):
            try:
                tmp = [(x[i] == strs[0][i]) for x in strs]
                print(tmp)
                if all(tmp):
                    c += 1
                else: 
                    break
            except IndexError:
                break
        return strs[0][:c]


try2 = Solution().longestCommonPrefix(strs=["aca","cba"])
print(try2)
try3 = Solution().longestCommonPrefix(strs=["flower","flow","flight"])
print(try3)