"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.   

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2]

"""
def twosum(nums,target):
    l=0
    r=len(nums)-1
    ans=[]
    while(l<=r):
        s=nums[l]+nums[r]
        if(s==target):
            ans=[l,r]
            break
        elif(s>target):
            r-=1
        elif(s<target):
            l+=1
    return ans
nums=[1,3,4,5,7,11]
target=11
print(twosum(nums,target))

