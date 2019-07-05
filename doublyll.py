class Node(object):
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    def getdata():
        return self.data
    def getNext():
        return self.next
    def getPrev():
        return self.prev
    def setNext(self,next_node):
        self.next=next_node
    def setPrev(self,prev_node):
        self.prev=prev_node

class DLL:
    def __init__(self,head=None):
        self.head=head
    def insert(data):
        newNode=Node(data)
        newNode.setNext(self.head)
        self.head.setPrev(newNode)
        self.head=newNode
    def size(self):
        current=self.head
        count=0
        while current:
            count=count+1
            current=current.getNext()
        return count
    def search(self,data):
        current=self.head
        found=False

        while current and found is False:
            if current.getdata()==data:
                found=True
            else:
                current=current.getNext
        if current is None:
            raise ValueError("Data not present in the list")
        return current
    def delete(self,data):
        current=self.head
        found=False
        while current and found is False:
            if current.getdata()==data:
                found=True 
            else:
                current=current.getNext()
        if current is None:
            raise ValueError("Data is not in the list")
        else:
            
            current.prev.setNext(current.next) 
            current.next.setPrev(current.prev)
            