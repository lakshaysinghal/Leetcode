class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        n=len(grid)
        m=len(grid[0])
        max_count=0
        
        for i in range(n):
            count=0
            for j in range(m):
                if grid[i][j]=="W":
                    count=0
                elif grid[i][j]=="E":
                    count+=1
                else:
                    grid[i][j]=count+int(grid[i][j])
            count=0
            for j in range(m-1,-1,-1):
                if grid[i][j]=="W":
                    count=0
                elif grid[i][j]=="E":
                    count+=1
                else:
                    grid[i][j]=count+int(grid[i][j])
        
        for j in range(m):
            count=0
            for i in range(n):
                if grid[i][j]=="W":
                    count=0
                elif grid[i][j]=="E":
                    count+=1
                else:
                    grid[i][j]=count+int(grid[i][j])
            count=0
            for i in range(n-1,-1,-1):
                if grid[i][j]=="W":
                    count=0
                elif grid[i][j]=="E":
                    count+=1
                else:
                    grid[i][j]=count+int(grid[i][j])
                    max_count=max(max_count,int(grid[i][j]))
                                  
        return max_count
# #O(N^3)
# class Solution:
#     def maxKilledEnemies(self, grid: List[List[str]]) -> int:
#         if not grid or not grid[0]:
#             return 0
#         n=len(grid)
#         m=len(grid[0])
#         max_count=0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j]=="0":
#                     count_h = 0
#                     for k in range(m):
#                         if grid[i][k]=="W":
#                             if k<j:
#                                 count_h=0
#                             else:
#                                 break
#                         if grid[i][k]=="E":
#                             count_h+=1
                    
#                     count_v = 0
#                     for k in range(n):
#                         if grid[k][j]=="W":
#                             if k<i:
#                                 count_v=0
#                             else:
#                                 break
#                         if grid[k][j]=="E":
#                             count_v+=1
                    
#                     max_count = max(max_count,count_h+count_v)
        
#         return max_count