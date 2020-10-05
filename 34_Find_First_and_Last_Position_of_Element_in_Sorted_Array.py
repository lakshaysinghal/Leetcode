class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.binarySearchLower(nums,0,len(nums)-1,target)
        if lower_bound == -1:
            return [-1,-1]
        return [lower_bound,self.binarySearchHigher(nums,0,len(nums)-1,target)]
        
    def binarySearchLower(self,nums,low,high,target):
        if high<low:
            return -1
        mid = (low+high)//2
        if nums[mid]==target:
            if mid>low and nums[mid]==nums[mid-1]:
                return self.binarySearchLower(nums,low,mid-1,target)
            else:
                return mid
        elif nums[mid]> :
            return self.binarySearchLower(nums,low,mid-1,target)
        return self.binarySearchLower(nums,mid+1,high,target)
    
    def binarySearchHigher(self,nums,low,high,target):
        if high<low:
            return -1
        mid = (low+high)//2
        if nums[mid]==target:
            if mid<high and nums[mid]==nums[mid+1]:
                self.binarySearchHigher(nums,mid+1,high,target)
            else:
                return mid
        elif nums[mid]>target:
            return self.binarySearchHigher(nums,low,mid-1,target)
        return self.binarySearchHigher(nums,mid+1,high,target)