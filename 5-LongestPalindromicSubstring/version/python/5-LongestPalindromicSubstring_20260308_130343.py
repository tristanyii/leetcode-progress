# Last updated: 3/8/2026, 1:03:43 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest = ""
4        
5        for i in range(len(s)):
6            for j in range(i, len(s)):
7                substring = s[i:j+1]
8                
9                if substring == substring[::-1]:  # check palindrome
10                    if len(substring) > len(longest):
11                        longest = substring
12                        
13        return longest