#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
    def addEdge(self,u,v): 
        self.graph[u].append(v)   
    def BFS(self, s): 
        queue1 =[]  
        queue2 =[]  
        if len(queue2) == 0 :   
            queue2.append(s)
            queue1.extend(self.graph[s])    
        while len(queue1) != 0 :
            for i in queue1:
                queue3=queue1+queue2
                queue2.append(i)
                queue1=queue1[1:]
                for j in self.graph[i]:
                    if j not in queue3:
                        queue1.append(j)
        return queue2
    def DFS(self, s):
        stack1=[]
        stack2=[]
        if len(stack2)==0:
            stack2.append(s)
            stack1.extend(self.graph[s])
        stack1=stack1[::-1]
        while len(stack1) != 0 :
            num = stack1[0]
            stack1=stack1[1:]
            stack2.append(num)
            for i in self.graph[num]:
                stack3=stack1+stack2
                if i not in stack3 :
                    stack1.insert(0,i)
        return stack2

