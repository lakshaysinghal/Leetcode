# 68ms
# Time  -O(log(N))
# Space -O(2**log(N))
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        while len(dp) < num+1: dp = dp + [val+1 for val in dp];
        return dp[:num+1]
        
# # 76 ms
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         dp = [0]
#         current = 1
#         while current <= num:
#             if current&(current-1) == 0:
#                 dp = dp + [val+1 for val in dp]
#                 current = current*2
#         return dp[:num+1]
# #~108ms-130ms
# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         if num == 0:
#             return [0]
#         elif num == 1:
#             return [0,1]
#         dp = [0,1,1]
#         lastsquare = 2
#         for i in range(3,num+1):
#             if i&(i-1) :
#                 dp.append(1 + dp[i-lastsquare])
#             else:
#                 dp.append(1)
#                 lastsquare = i
#         return dp
        

sol = Solution()
print(sol.countBits(3))