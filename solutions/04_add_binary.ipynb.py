class Solution:
    def addBinary(self, a, b):
        num_a = int(a, 2)
        num_b = int(b, 2)
        total = num_a + num_b
        return bin(total)[2:]
