'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=j=0
        dic={}
        for i,c in enumerate(s):
            if c in dic:
                j=max(j,dic[c])
            dic[c]=i+1
            l= max(l,i-j+1)
        return l
