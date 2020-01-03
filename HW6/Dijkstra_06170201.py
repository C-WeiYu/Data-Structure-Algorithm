#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.weight = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
    def addEdge(self,u,v,w): 
        self.weight.append([u,v,w])
        self.weight=sorted(self.weight,key=lambda x:x[2])      
    def Dijkstra(self, s): 
        a=0
        dict={}
        left_list=[]
        distance_list=[math.inf]*self.V
        for i in range(self.V):
            if i == s:
                distance_list[i]=0
        while len(left_list) < self.V:  
            distance_list_modify = sorted(distance_list)
            for j in range(self.V):
                if distance_list[j]==distance_list_modify[a] and j not in left_list:
                    left_list.append(j)
                    break
            if j == 0 :
                for k in range(self.V): 
                    if distance_list[k] == math.inf:
                        if self.graph[j][k] != 0 :
                            distance_list[k]=self.graph[j][k]
                        else:
                            pass
                    else:
                        pass
            else:
                for h in range(self.V):       
                    if distance_list[h] == math.inf:
                        if self.graph[j][h] != 0 :
                            distance_list[h]=distance_list[j]+self.graph[j][h] #對
                        else:
                            pass
                    else:
                        if self.graph[j][h]!=0:
                            if distance_list[h] > distance_list[j]+self.graph[j][h]:
                                distance_list[h]=distance_list[j]+self.graph[j][h]
                            else:
                                pass
                        else:
                            pass
            a+=1
        for x in range(self.V):
            dict[str(x)]=distance_list[x]
        return dict
    def Kruskal(self):
        parent=[]
        dict={}
        for i in range(self.V):
            parent.append(i)
        right=[]
        for vertix in self.weight:
            if parent[vertix[0]] == parent[vertix[1]] :
                pass
            else:
                right.append(vertix)
                for j in range(self.V):
                    if parent[j]==parent[vertix[1]]:
                        parent[j]=parent[vertix[0]]
                parent[vertix[1]] ==parent[vertix[0]]

        for k in right:
            name='{}-{}'.format(k[0],k[1])
            dict[name]=k[2]                
        return dict   

