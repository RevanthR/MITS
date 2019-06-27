class Node(object):
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setNext(self,new):
        self.next=new

class LinkedList(object):
    def __init__(self,head=None):
        self.head=head
    
    def insert(self,data):
        newNode=Node(data)
        newNode.setNext(self.head)
        self.head=newNode
    def size(self):
        current=self.head
        count=0
        while curret:
            count=count+1
            current=current.getNext()
        return count
    def search(self,data):
        current=self.head
        found=False
        while current and found is False:
            if current.getData()==data:
                found=True
            else:
                current=current.getNext()
        if current is None:
            raise ValueError("Data is not in the list")
        return current
    def delete(self,data):
        current=self.head
        found=False
        previous=None
        while current and found is False:
            if current.getData()==data:
                found=True
            else:
                previous=current
                current=current.getNext()
        if current is None:
            raise ValueError("Data is not in the list")
        if previous is None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext()) 
    def display(self):
        current=self.head
        if current is None:
            print("List is Empty")
        else:
            print("The following is the Linked List")
            while current:
                
                print(current.data,end=" ")
                current=current.getNext()          
if __name__ == "__main__":
    l=LinkedList()
    l.insert(20)
    l.insert(30)
    l.delete(30)
    l.display()
    