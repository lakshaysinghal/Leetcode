#O(N)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        length=0
        l=0
        r=1
        mp={}
        mp[s[0]]=1
        while r<len(s):
            mp[s[r]]=mp.get(s[r],0)+1
            if len(mp)<=2:
                length = max(length,r-l+1)
            while len(mp)>2:
                mp[s[l]]-=1
                if mp[s[l]]==0:
                    del mp[s[l]]
                l+=1
            length = max(length,r-l+1)
            r+=1
                
        return length
# #O(N^2)
# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         if not s:
#             return 0
#         if len(s)==1:
#             return 1
#         length=0
#         for i in range(len(s)-1):
#             j=i+1
#             mp={}
#             mp[s[i]]=1
#             while j<len(s):
#                 mp[s[j]]=mp.get(j,0)+1
#                 count = len(mp)
#                 if count>3:
#                     break
#                 if count<=2:
#                     length = max(length,j-i+1)
#                 j+=1
#         return length