class Solution:
    def assignBikes(self, workers: [[int]], bikes: [[int]]) -> [int]:
        workerBikePair = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                workerBikePair.append((self.manhattanDistance(workers[i],bikes[j]),i,j))
        workerBikePair.sort()
        isBikeAssigned={x:False for x in range(len(bikes))}
        assignment=[-1 for i in range(len(workers))]
        for i in range(len(workerBikePair)):
            if assignment[workerBikePair[i][1]]==-1 and not isBikeAssigned[workerBikePair[i][2]]:
                assignment[workerBikePair[i][1]]=workerBikePair[i][2]
                isBikeAssigned[workerBikePair[i][2]]=True
        return assignment
    def manhattanDistance(self,p1,p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

print(Solution().assignBikes([[0,0],[2,1]],[[1,2],[3,3]]))