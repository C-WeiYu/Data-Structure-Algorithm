"""定義Node"""
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
 """定義LinkedList"""
class MyLinkedList:
    
          """
        基本結構
          """
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0


          """
    取得某位置的數據
          """
  def get(self, index: int) -> None:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        a=self.head
        for i in range(index):
            a=a.next
        return a.val
        
        
        
         """
      開頭加Node
         """
    def addAtHead(self, val: int) -> None:
        newHead=Node(val)
        newHead.next=self.head
        self.head=newHead
        self.size = self.size + 1
        
        
        
         """
      尾巴加Node
         """
    def addAtTail(self, val: int) -> None:
        a=self.head
        if a is None:
            self.head=Node(val)
        else:
            while a.next is not None:
                a=a.next
            a.next=Node(val)         
        self.size = self.size+1




         """
      中間加Node
         """
  def addAtIndex(self, index: int, val: int) -> None:      
        if index < 0 and index != -1:
            pass
        elif index > self.size:
            pass
        elif index == self.size or index == -1:
            self.addAtTail(val)

        elif index == 0:
            self.addAtHead(val)
        else:
            a = self.head
            for i in range(index - 1):
                a = a.next
            node = Node(val)
            node.next = a.next
            a.next = node

            self.size += 1

         """
      刪除其中Node
         """
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        a = self.head
        if index == 0:
            self.head = a.next
        else:
            for i in range(index - 1):
                a = a.next
            a.next = a.next.next

        self.size -= 1


