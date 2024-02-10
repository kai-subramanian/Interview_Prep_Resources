"""
LC 1 - Two sum.
Given an array of integers and a target integer, 
find two numbers from the array that add up to target
You can return in any order.
"""

l=[2,4,9,6,1,3]
TARGET=15

# Brute force approach - scan twice and find two nums that sum up to target.
for i in range (0, len(l)):
    for j in range (i, len(l)):
        if(l[i]+l[j]==TARGET):
            ans=[i,j]

print("Brute Force - ",ans)

# Optimised approach - initialize a hashmap, and check if the complement (target - number)
# exists in the map. If so, return the number else add to hashmap

hashmap={} # stores value, index in key,value format.
for i in range(0,len(l)):
    diff=TARGET-l[i]
    if diff in hashmap:
        print("Optimized approach - ",[hashmap[diff],i])
    hashmap[l[i]]=i