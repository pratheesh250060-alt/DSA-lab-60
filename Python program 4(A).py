class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if self.head is None:
            print("List is Empty")
            return
        while temp:
            print(temp.data, "--->", end=" ")
            temp = temp.next
        print()

    def insert_beginning(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_end(self, data):
        ne = Node(data)
        if self.head is None:
            self.head = ne
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insert_position(self, pos, data):
        np = Node(data)
        if pos == 1:
            np.next = self.head
            self.head = np
            return
        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        np.next = temp.next
        temp.next = np

    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        prev = self.head
        temp = self.head.next
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def delete_position(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos - 2):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next
        temp.next = temp.next.next if temp.next else None


# Demo
obj = LL()
obj.insert_end(10)
obj.insert_end(20)
obj.insert_end(30)

print("DISPLAY THE CREATED LIST ..... ")
obj.display()

obj.insert_beginning(5)
print("AFTER INSERTING 5 AT THE BEGINNING.... ")
obj.display()

obj.insert_end(40)
print("INSERTING 40 AT THE END OF THE LIST")
obj.display()

obj.insert_position(3, 25)
print("INSERTING 25 AT THE MIDDLE OF THE LIST")
obj.display()

obj.delete_beginning()
print("AFTER DELETING THE FIRST NODE 5 FROM THE LIST...")
obj.display()

obj.delete_end()
print("AFTER DELETING THE LAST NODE 40 FROM THE LIST...")
obj.display()

obj.delete_position(3)
print("AFTER DELETING MIDDLE NODE 25 FROM THE LIST...")
obj.display()


