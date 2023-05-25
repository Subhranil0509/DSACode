class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current is not None:
            if current.data == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"{value} not found in the Linked List.")

    def delete_at_position(self, position):
        if self.head is None:
            print("Linked List is empty.")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0
        while current is not None:
            if count == position:
                prev.next = current.next
                return
            count += 1
            prev = current
            current = current.next

        print("Invalid position.")

    def delete_linked_list(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked List is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" -> ")
                current = current.next
            print("None")


# Example usage
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)

linked_list.display()  # Output: 10 -> 20 -> 30 -> 40 -> None

linked_list.delete_by_value(20)
linked_list.display()  # Output: 10 -> 30 -> 40 -> None

linked_list.delete_at_position(1)
linked_list.display()  # Output: 10 -> 40 -> None

linked_list.delete_linked_list()
linked_list.display()  # Output: Linked List is empty.
