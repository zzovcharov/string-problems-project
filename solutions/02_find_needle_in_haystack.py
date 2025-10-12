class Solution:
    def strStr(self, haystack, needle):
        n = len(needle)
        h = len(haystack)

        for i in range(h - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1
