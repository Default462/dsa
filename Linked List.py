class LinkeList:
    def __init__(self):
        self.head=None
class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

    def insert(self, prev_node,data):
        self.data = data
        self.next = prev_node.next
        prev_node.next = self.data

    def delete(self , data):
        if self.head is None:
            return "List is empty"
        while self.data == data:
            self.data = self.next
        pass



