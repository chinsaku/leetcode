class Solution:
    def isPalindrome(self, x: int) -> bool:

        is_minus = False
        str_x = str(x)
        if str_x[0] == '-':
            str_x = str_x[1:]
            #is_minus = True

        ver = str_x[::-1]
        #if is_minus:
        #ver = '-'+ ver

        if x == int(ver):
            return True
        else:
            return False
