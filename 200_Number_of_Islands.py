class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []:
            return 0
        numIsland = 0
        n = len(grid)
        m = len(grid[0])
        temp=[[0]*(m+2)]
        graph={}
        for i in range(n):
            c=[0]
            for j in range(m):
                c.append(grid[i][j])
            c.append(0)
            temp.append(c)
        temp+=[[0]*(m+2)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if temp[i][j]=="1":
                    if temp[i+1][j]=="1":
                        graph[(i,j)]=graph.get((i,j),[])+[(i+1,j)]
                        graph[(i+1,j)]=graph.get((i+1,j),[])+[(i,j)]
                    if temp[i][j+1]=="1":
                        graph[(i,j)]=graph.get((i,j),[])+[(i,j+1)]
                        graph[(i,j+1)]=graph.get((i,j+1),[])+[(i,j)]
        
        q=[]
        visited={}
        for i in range(1,n+1):
            for j in range(1,m+1):
                if temp[i][j]=="1" and not visited.get((i,j),False):
                    numIsland+=1
                    q.append((i,j))
                    visited[(i,j)]=True
                    while(len(q)):
                        current = q.pop(0)
                        ii=current[0]
                        jj=current[1]
                        if temp[ii][jj+1] =="1" and not visited.get((ii,jj+1),False):
                            q.append((ii,jj+1))
                            visited[(ii,jj+1)] = True
                        if temp[ii+1][jj] =="1" and not visited.get((ii+1,jj),False):
                            visited[(ii+1,jj)]=True
                            q.append((ii+1,jj))
                        if temp[ii][jj-1] =="1" and not visited.get((ii,jj-1),False):
                            q.append((ii,jj-1))
                            visited[(ii,jj-1)] = True
                        if temp[ii-1][jj] =="1" and not visited.get((ii-1,jj),False):
                            visited[(ii-1,jj)]=True
                            q.append((ii-1,jj))
        return numIsland               