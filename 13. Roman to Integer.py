class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dictx = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
            if i == 0:
                sum += dictx[s[i]]
            elif ((s[i] == 'V' or s[i] =='X') and (s[i - 1] == 'I')):
                sum = sum + dictx[s[i]] - 2
            elif ((s[i] == 'L' or s[i] =='C') and (s[i - 1] == 'X')):
                sum = sum + dictx[s[i]] - 20
            elif ((s[i] == 'D' or s[i] =='M') and (s[i - 1] == 'C')):
                sum = sum + dictx[s[i]] - 200
            else:
                sum = sum + dictx[s[i]]

        return sum


a = Solution().romanToInt(s="MCMXCIV")
print(a)
# print(len("VII"))
# I, V, X, L, C, D and M