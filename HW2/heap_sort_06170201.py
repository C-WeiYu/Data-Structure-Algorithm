#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Solution(object):
    def heapify(self,nums,root,length):
        left=2*root+1
        right=2*root+2

        if left < length and right <length:
            if nums[left]>nums[right]:
                if nums[left]>nums[root]:
                    Max=left
                else:
                    Max=root
            else:
                if nums[right]>nums[root]:
                    Max=right
                else:
                    Max=root
        elif left<length and right>=length:
            if nums[left]>nums[root]:
                Max=left
            else:
                Max=root
        else:
            Max=root
        if Max != root :
            heapify_temp_root=nums[root]
            nums[root] =nums[Max]
            nums[Max]=heapify_temp_root
            Solution.heapify(self,nums,Max,length)
        
    def heap_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        ans=[]
        n=len(nums)
        if n%2 == 0:
            for root in range((n//2)-1,-1,-1):
                Solution.heapify(self,nums,root,n)
        else:
            for root in range(((n-1)//2)-1,-1,-1):
                Solution.heapify(self,nums,root,n)
            
        for i in range(0,n):
            ans.append(nums[0])
            nums[0]=nums[n-1]
            del nums[n-1]
            n=n-1
            Solution.heapify(self,nums,0,n)
        ans=ans[::-1]
        return ans
        


# In[8]:


ans=Solution().heap_sort([3,2,1,4,5])
ans


# In[9]:


ans=Solution().heap_sort([3,4,5,-6,3,2,1,6,2,8,5])
ans

