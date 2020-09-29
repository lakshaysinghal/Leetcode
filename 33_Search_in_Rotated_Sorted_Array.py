class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index =-1
        for i in range(len(nums)):
            if target == nums[i]:
                index = i
                break
        
        return index

'''
##Alternative Solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivotPosition(nums,0,len(nums)-1)
        if(pivot ==-1):
            return self.binarySearch(nums,0,len(nums)-1,target)
        elif(target == nums[pivot]):
            return pivot
        #elif target<=nums[-1]:
            #index= self.binarySearch(nums,pivot+1,len(nums)-1,target)
        elif target>=nums[0]:
            return self.binarySearch(nums,0,pivot-1,target)
        return self.binarySearch(nums,pivot+1,len(nums)-1,target)
        
    def pivotPosition(self,nums,low,high):
        if high<low:
            return -1
        if high==low:
            return low
        mid = (high+low)//2
        
        if(mid<high and nums[mid]>nums[mid+1]):
            return mid
        if(mid>low and nums[mid]<nums[mid-1]):
            return mid-1
        
        if(nums[mid]<=nums[low]):
            return self.pivotPosition(nums,low,mid-1)
        return self.pivotPosition(nums,mid+1,high)
           
    def binarySearch(self,nums,low,high,target):
        if high<low:
            return -1
        mid = (high+low)//2
        
        if(nums[mid]==target):
            return mid
        elif(nums[mid]>target):
            return self.binarySearch(nums,low,mid-1,target)
        else:
            return self.binarySearch(nums,mid+1,high,target)
'''