class Solution:
    def reverse(self, x: int) -> int:

        m = str(x)
        is_minus = False
        if m[0] == '-':
            m = m[1:]
            is_minus = True

        rever_m = m[::-1]
        if is_minus:
            rever_m = '-' + rever_m

        rever_m = int(rever_m)

        if rever_m > 2**31 - 1 or rever_m < -2**31:
            return 0
        return rever_m


t = Solution().reverse(x=32)
print(t)