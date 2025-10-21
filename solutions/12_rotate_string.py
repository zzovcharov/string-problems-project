class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False