#!/usr/bin/env python
# coding: utf-8

# In[42]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """


class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root:
            if val <= root.val:
                if root.left:
                    return Solution.insert(self, root.left, val)
                else:
                    node = TreeNode(val)
                    root.left = node
                    return root.left
            else:
                if root.right:
                    return Solution.insert(self, root.right, val)
                else:
                    node = TreeNode(val)
                    root.right = node
                    return root.right
        else:
            root=TreeNode(val)
            return root

    def delete(self, root, target):
        a = []
        Solution.Preorder(self, root, target, a)
        for i in a:
            if i == target:  # 用改用get_Max
                if root:
                    if target < root.val:
                        root.left = Solution.delete(self, root.left, target)
                    elif target > root.val:
                        root.right = Solution.delete(self, root.right, target)
                    elif target == root.val:
                        return Solution.delete_by(self, root)
                else:
                    pass
        return root

    def delete_by(self,root):
        if root.left:
            if root.right:
                Max_node = Solution.get_Max(self,root.left)
                root.val=Max_node.val
                root.left=Solution.delete(self,root.left,Max_node.val)
                return root
            else:
                return root.left
        else:
            if root.right:
                return root.right
            else:
                return None
    def get_Max(self,c_root):
        if c_root.right:
            return Solution.get_Max(self,c_root.right)
        else:
            return c_root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root:
            if target < root.val:
                return Solution.search(self, root.left, target)
            elif target > root.val:
                return Solution.search(self, root.right, target)
            elif target == root.val:
                return root
        else:  # 當target根本不存在於Tree中
            return None

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """
        b = []
        b = Solution.Preorder_for_modify(self, root, target, new_val, b)
        root_index = int(len(b)/2)
        root1 = TreeNode(b[root_index])
        #root = Solution.rebuild_bst(self, b, center)
        Solution.rebuild_bst(self, b[:root_index], root1)
        Solution.rebuild_bst(self, b[root_index+1:], root1)
        return root1
        # def modify_new(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype: None Do not return anything, modify nodes(maybe more than more) in-place instead.(cannot search())
        """

    #    Solution.delete(self,root,target)
    #    Solution.insert(self,root,new_val)
    #    return root
    def Preorder(self, root, target, a):
        if root:
            a.append(root.val)
            Solution.Preorder(self, root.left, target, a)
            Solution.Preorder(self, root.right, target, a)

    def Preorder_for_modify(self, root, target, new_val, nums):
        if root:
            nums.append(root.val)
            Solution.Preorder_for_modify(self, root.left, target, new_val, nums)
            Solution.Preorder_for_modify(self, root.right, target, new_val, nums)
        for j in range(0, len(nums)):
            if nums[j] == target:
                nums[j]=new_val
        for k in range(len(nums)):
            if k + 1 < len(nums) :
                if nums[k] > nums[k + 1]:
                    nums[k], nums[k + 1] = nums[k + 1], nums[k]
        return nums

    def insert_for_modify(self, root, val):
        if root==None:
            root = TreeNode(val)
            return root
        else:
            if val <= root.val:
                if root.left:
                    return Solution.insert_for_modify(self, root.left, val)
                else:
                    node = TreeNode(val)
                    root.left = node
                    return root.left
            else:
                if root.right:
                    return Solution.insert_for_modify(self, root.right, val)
                else:
                    node = TreeNode(val)
                    root.right = node
                    return root.right

    def rebuild_bst(self, nums, center):
        if not nums:
            return None
        else:
            root_index = int(len(nums) / 2)
            new_root = Solution.insert_for_modify(self, center, nums[root_index])
            Solution.rebuild_bst(self, nums[:root_index], center)
            Solution.rebuild_bst(self, nums[root_index+1:], center)


# In[47]:


root = TreeNode(5)
node1 = TreeNode(3)
node2 = TreeNode(3)
node3 = TreeNode(-5)
node4 = TreeNode(8)
node5 = TreeNode(7)
node6 = TreeNode(6)
node7 = TreeNode(10)
root.left = node1
root.left.left = node2
root.left.left.left = node3
root.right = node4
root.right.left = node5
root.right.left.left = node6
root.right.right = node7


# In[48]:


print("delete")
root2=Solution().delete(root,3)
print(root2.val==5 and root2.left.val==-5 and root2.left.left==None and root2.left.right==None)
print(root2.right.right.val==10 and root2.right.left.val==7 and root2.right.left.left.val==6)
print(root2.right.right.right==None and root2.right.right.left==None and root2.right.left.right==None)
print(root2.right.left.left.left==None and root2.right.left.left.right==None and root2.right.val==8)


# In[44]:


print("insert")
print(Solution().insert(root,4)==root.left.right)


# In[46]:


print("modify")
print(Solution().search(root,10)==root.right.right)

