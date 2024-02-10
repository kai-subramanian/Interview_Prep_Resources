def search(nums,target):
        l=0
        r=len(nums)-1
        ans=-1
        while(l<=r):
            mid=(l+r)//2
            print(mid)
            if(nums[mid]==target):
                ans=mid
                break
            elif(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                r=mid-1
        return ans

nums=[0,1,2,3,4,6,9,11]
print(search(nums,6))