class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None

    def add(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
        else:
            temp = self.start
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def show(self):
        if self.start is None:
            print("List is empty")
            return
        temp = self.start
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")

    def delete(self, position):
        if self.start is None:
            print("List is empty")
            return
        if position <= 0:
            print("Invalid position")
            return
        if position == 1:
            self.start = self.start.next
            return
        temp = self.start
        count = 1
        while temp and count < position - 1:
            temp = temp.next
            count += 1
        if temp is None or temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next

list1 = LinkedList()

while True:
    print("\n1. Add value")
    print("2. Show list")
    print("3. Delete position")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        val = input("Enter value to add: ")
        list1.add(val)
    elif choice == "2":
        list1.show()
    elif choice == "3":
        pos = int(input("Enter position to delete: "))
        list1.delete(pos)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
