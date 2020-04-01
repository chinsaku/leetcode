class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        score = 0
        for i in range(len(s)-1,-1,-1):
            if score !=0 and s[i] == ' ':
                break
            if s[i] != ' ':
                score += 1
        return score



class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])
