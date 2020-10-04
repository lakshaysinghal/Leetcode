class Solution:
    def fourSum(self, nums, target: int):
        sumOfTwo = {}
        result = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):

                sumValue=nums[i]+nums[j]
                sumOfTwo[sumValue] = sumOfTwo.get(sumValue,[])+[(i,j)]
                
                if sumOfTwo.get(target-sumValue,False):
                
                    for (x,y) in sumOfTwo[target-sumValue]:
                        if x != i and x!=j and y!=i and y!=j:
                            quad = [nums[i],nums[j],nums[x],nums[y]]
                            quad.sort()
                            if quad not in result:
                                result.append(quad)
        return result

print(Solution().fourSum([0,0,0,0],0))