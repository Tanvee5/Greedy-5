# Problem 1 : Wildcard Matching
# Time Complexity : 
'''
DP 2-d array - O(m*n) where m is the length of the source string and n is the length of the pattern string
DP 1-d array - O(m*n) where m is the length of the source string and n is the length of the pattern string
Two Pointer -  O(m*n) where m is the length of the source string and n is the length of the pattern string
'''
# Space Complexity :
'''
DP 2-d array - O(m*n) where m is the length of the source string and n is the length of the pattern string
DP 1-d array - O(m) where m is the length of the source string
Two Pointer -  O(1)
''' 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

# Dp Solution 2-d array
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # get the length of the source and pattern string
        m = len(s)
        n = len(p)
        # define dp matrix with size (m+1 * n+1) and set the value to False
        dp = [[False] * (m+1) for _ in range(n+1)]
        # set the value of dp[0][0] as True
        dp[0][0] = True

        # loop from 1 to n+1 ie 1st column
        for i in range(1, n+1):
            # check if the character of p at (i-1)th position is '*'
            if p[i-1] == '*':
                # if it is then set the the value of dp[i][0] to value of prev dp ie dp[i-1][0]
                dp[i][0] = dp[i-1][0]
            else:
                # else set the value of dp[i][0] t0 False
                dp[i][0] = False
        
        # loop from 1 to n+1
        for i in range(1, n+1):
            # loop from 1 to m+1
            for j in range(1, m+1):
                # get the character of pattern at (i-1)th position and character of source at (j-1)th position
                pChar = p[i-1]
                sChar = s[j-1]
                # check the character of pattern is '*' 
                if pChar == '*':
                    # if it is then set the value of dp[i][j] to value of previous element(dp[i-1][j]) or to the value of above element(dp[i][j-1])
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    # else check if the character of pattern are equal to source or character of pattern is '?'
                    if pChar == sChar or pChar == '?':
                        # if it is then set the value of dp to value of diagonal element (dp[i-1][j-1])
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        # else set the value of dp[i][j] to False
                        dp[i][j] = False
        # return the value of dp[n][m]
        return dp[n][m]


# Dp Solution 1-d array
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # get the length of the source and pattern string
        m = len(s)
        n = len(p)
        # define dp matrix with size (m+1) and set the value to False
        dp = [False] * (m+1)
        # set the value of dp[0][0] as True
        dp[0] = True
        
        # loop from 1 to n+1
        for i in range(1, n+1):
            # define diagUp and set to False
            diagUp = False
            # loop from 1 to m+1
            for j in range(m+1):
                # save the value of dp[j] in temp variable
                temp = dp[j]
                # get the character of pattern at (i-1)th position
                pChar = p[i-1]
                # check the character of pattern is '*' 
                if pChar == '*':
                    # check if j is 0
                    if j == 0:
                        # if it is then set the value of dp[j] as dp[j]
                        dp[j] = dp[j]
                    else:
                        # else set the value of dp[j] as dp[j] or value of previous element(dp[j-1])
                        dp[j] = dp[j] or dp[j-1]
                else:
                    # else check if j is 0
                    if j == 0:
                        # if it is value of dp[j] as False
                        dp[j] = False
                    else:
                        # else get the character of source ar (j-1)th position
                        sChar = s[j-1]
                        # check if the character of pattern are equal to source or character of pattern is '?'
                        if pChar == sChar or pChar == '?':
                            # set the value of dp[j] to diagUp
                            dp[j] = diagUp
                        else:
                            # else set the value of dp[j] to False
                            dp[j] = False
                # store the value of temp in diagUp
                diagUp = temp
        # return the value of dp[m]
        return dp[m]

# Two pointer solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # get the length of the source and pattern string
        sl = len(s)
        pl = len(p)
        # define sp and pp pointer for source and pattern and set the value as 0
        sp = 0
        pp = 0
        # define the sStar and pStart for source and pattern (placeholder for star position) and set to -1
        sStar = -1
        pStar = -1

        # loop till sp is less than sl
        while sp < sl:
            # check if pp is less than pl and character of source at sp are equal to character of pattern at pp or character of pattern at pp is '?'
            if pp < pl and (s[sp] == p[pp] or p[pp] == '?'):
                # if it is then increment the sp and pp value
                sp += 1
                pp += 1
            # check if pp is less than ppl and character of pattern at pp is '*'
            elif pp < pl and p[pp] == '*':
                # if it is then set the value of sStar to sp and pStar to pp
                sStar = sp
                pStar = pp
                # increment the pp value
                pp += 1
            # check if value of pStar is -1 ie there is no star in the string
            elif pStar == -1:
                # return False
                return False
            else:
                # else increment the sStar
                sStar += 1
                # set sp to sStar and pp to pStar + 1
                sp = sStar
                pp = pStar + 1

        # loop till pp is less than pl
        while pp < pl:
            # check if the character of pattern at pp is '*'
            if p[pp] == '*':
                # if it is then increment the pp 
                pp += 1
            else:
                # else return False
                return False

        # return True
        return True 
    