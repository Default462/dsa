class LinkeList:
    def __init__(self):
        self.head=None

    def printList(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.next)
            temp_node=temp_node.next
class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

    def insert_in_between(self,data, prev_node=None ):
        temp_node = Node(data)
        if prev_node is None:
            temp_node.next = self.head
            self.head = temp_node
        
        temp_node.next = prev_node.next
        prev_node.next = temp_node

    def append(self, data):
        temp_node=Node(data)
        cur_node=self.head
        while cur_node.next:
            cur_node=cur_node.next
        cur_node.next=temp_node

    def delete(self,data,previous_node=None):
        if self.head is None:
            return ("List is empty")
        current_node=self.head
        while current_node:
            if current_node.data==data:
                if current_node.next is None:
                    current_node.data=None
                previous_node.next = current_node.next
                current_node=current_node.next



