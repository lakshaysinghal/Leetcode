# DP O(N) time & space
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        isWordBreakableTillPos=[False]*len(s)
        wordDict_dict = {word:1 for word in wordDict}
        for i in range(len(s)):
            if s[:i+1] in wordDict_dict:
                isWordBreakableTillPos[i]=True
                continue
            for j in range(i):
                if isWordBreakableTillPos[j] and s[j+1:i+1] in wordDict_dict:
                    isWordBreakableTillPos[i]=True
                    break
        return isWordBreakableTillPos[-1]
# #recursive + memo
# class Solution:
#     dp={}
#     def wordBreak(self, s: str, wordDict) -> bool:
#         if not s:
#             return True
#         if (s in self.dp) or (s in wordDict):
#             self.dp[s]=True
#             return True
#         for i in range(1,len(s)-1):
#             flag = self.wordBreak(s[:i],wordDict) and self.wordBreak(s[i:],wordDict)
#             if flag:
#                 self.dp[s]=True
#                 return True
#         return False