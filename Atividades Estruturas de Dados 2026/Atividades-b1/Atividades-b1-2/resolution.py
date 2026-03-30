class Node:
    def __init__(self, val=None):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get_by_index(self, index):
        current_position = 0
        current = self.head
        while current is not None:
            if current_position == index:
                return current
            current_position += 1
            current = current.next
        print(f"The index {index} doesn't exists on list")
        return None

    def remove(self, position):
        current = self.head
        current_position = 0

        if position == 0:
            self.head = current.next
            return

        while current is not None:
            if current_position + 1 == position:
                if current.next is None:
                    print(f"Position {position} doesn't exists on the list")
                    return
                current.next = current.next.next
                return
            current = current.next
            current_position += 1

        print(f"The position {position} doesn't exists on the list")

    def remove_element(self, val):
        current = self.head

        if current is None:
            print("The list is already empty!")
            return

        if current.val == val:
            self.head = current.next
            return

        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next

        print(f"Element {val} isn't on the list")

    def insert(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_on_start(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_on_position(self, position, val):
        new_node = Node(val)
        current_position = 0
        current = self.head
        while current is not None:
            if current_position == position:
                new_node.next = current.next
                current.next = new_node
                return
            current_position += 1
            current = current.next
        print(f"The position {position} doesn't exists on list")

    def list_all(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next


mylist = LinkedList()

mylist.insert(1)
mylist.insert(2)
mylist.insert(3)
mylist.insert(4)
mylist.insert(5)

index = int(input("Enter an index: "))
node = mylist.get_by_index(index)

if node is not None:
    print(f"Node at {index}: {node.val}")