class Solution(object):
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        
        for i in range(len(strs[0])):       # loop through characters of first word
            for word in strs:                  # loop through every string
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:i]         # return prefix up to mismatch
        
        return strs[0]                         # all characters matched