'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"
'''
def longestPalindrome(s):
    res=''
    resLen = 0
    
    for i in range(len(s)):
        l,r = i,i
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r-l+1)>len(res):
                res = s[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1
        l,r = i,i+1
        while l>=0 and r<len(s) and s[l] == s[r]:
            if (r-l+1)>len(resLen):
                res = s[l:r+1]
                resLen = r-l+1
            l-=1
            r+=1
    return res


s = 'babad'
print(longestPalindrome(s))