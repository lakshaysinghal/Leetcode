class Solution:
    def findMissingRanges(self, nums: [int], lower: int, upper: int) -> [str]:
        if not nums:
            return [self.returnRange(lower,upper)]
        # if lower==upper and len(nums)==1:
        #     return []
        
        lowerRange=lower
        result=[]
        for num in nums:
            if num==lowerRange:
                lowerRange+=1
            else:
                result.append(self.returnRange(lowerRange,num-1))
                lowerRange=num+1
        if lowerRange <= upper:
            result.append(self.returnRange(lowerRange,upper))
        return result
        
    def returnRange(self,lower,upper):
        if lower==upper:
            return str(lower)
        else:
            return str(lower)+"->"+str(upper)

print(Solution().findMissingRanges([-1],-1,0))