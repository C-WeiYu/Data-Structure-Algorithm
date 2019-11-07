#!/usr/bin/env python
# coding: utf-8

# In[1]:


###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        i=0
        j=0
        left=[]
        right=[]
        ans=[]
        if len(nums)<=1:
            return nums
        else:
            if len(nums)%2 == 0 :
                left=nums[0:int(len(nums)/2)]
                right=nums[int(len(nums)/2) : len(nums)]
            else :
                left=nums[0:(len(nums)+1)//2]
                right=nums[(len(nums)+1)//2:len(nums)]
        left=self.merge_sort(left)
        right=self.merge_sort(right)
        while len(ans)!= len(left+right):
            if left[i]>right[j]:
                ans.append(right[j])
                j+=1
            elif left[i]==right[j]:
                ans.append(right[j])
                j+=1
            elif left[i]<right[j]:
                ans.append(left[i])
                i+=1
            while i==len(left) and j != len(right):
                ans.append(right[j])
                j+=1
            while j==len(right) and i != len(left):
                ans.append(left[i])
                i+=1
        return ans        


# In[2]:


ans=Solution().merge_sort([22,1,15,2,-4,5,3])
ans

