class Solution:
    def reverse(self, x: int) -> int:

        outcome = 0
        list = []
        while x / 10:
            list.append(x / 10)
            x = x / 10

        for i in range(len(list)):
            outcome = (outcome + list[i]) * 10
