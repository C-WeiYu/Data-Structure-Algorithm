#!/usr/bin/env python
# coding: utf-8

# In[28]:


from Cryptodome.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    def add(self, key):
        key_int = MyHashSet.Hash(self, key)
        index = key_int % self.capacity
        node_head=self.data[index]
        if node_head:
            while node_head.next:
                if node_head.val == key_int:  
                    return
                else:
                    node_head=node_head.next  
            if node_head.val != key_int:
                node_head.next=ListNode(key_int) 
            else:
                return
        else:
            node_head=ListNode(key_int)
            self.data[index]=node_head
    def remove(self, key):
        key_int = MyHashSet.Hash(self, key)
        index = key_int % self.capacity
        node_head = self.data[index]
        if node_head:
            if node_head.val == key_int :
                node_head=node_head.next
                self.data[index] = node_head
        if node_head : 
            while node_head.next:
                if node_head.next.val == key_int:
                    node_head.next = node_head.next.next
                else:
                    node_head = node_head.next
    def contains(self, key):
        key_int = MyHashSet.Hash(self, key)
        index = key_int % self.capacity
        node_head=self.data[index]
        while node_head != None:
            if node_head.val == key_int:
                return True
            else:
                node_head = node_head.next
        else:
            return False
    def Hash(self, key):
        h = MD5.new()
        h.update(key.encode('utf-8'))
        new_key=int(h.hexdigest(),16)
        return new_key

