class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=[]

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.queue==[]:
            pass
        else:
            A=self.queue[0]
            self.queue=self.queue[1:]
            return A
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.queue[0]
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.queue==[]:
            return True
        else:
            return False
