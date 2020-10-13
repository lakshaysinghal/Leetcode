class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict={}
        res=[]
        for i in range(len(nums)):
            if target-nums[i] in numDict:
                return [numDict[target-nums[i]],i]
            numDict[nums[i]]=i
        