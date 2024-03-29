class Stack:  # create a stack class
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    
    s=Stack() #creating a stack object

    print(s.isEmpty())

    s.push(4)
    s.push('dog')
    print(s.top())
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())
