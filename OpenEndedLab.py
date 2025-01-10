class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node (default is None)
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Start with an empty list
        self.head = None

    def append(self, data):
        # Create a new node and add it to the end of the list
        new_node = Node(data)
        
        if not self.head:  # If the list is empty, make this node the head
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next  # Traverse until the last node
            current.next = new_node  # Attach the new node at the end

    def display(self):
        # Show all elements in the list, with an arrow separating them
        if not self.head:
            print("The list is empty!")  # Handle the case of an empty list
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Display each node's data
            current = current.next
        print("None")  # End of the list

    def delete_after_m_skip_n(self, m, n):
        if m < 0 or n < 0:
            print("Skip and delete counts can't be negative!")
            return
        
        current = self.head
        while current:
            # Skip m nodes
            for _ in range(m):
                if not current.next:
                    return  # Exit if we've reached the end
                current = current.next
            
            # Now delete the next n nodes
            node_to_delete = current.next
            for _ in range(n):
                if not node_to_delete:
                    break
                node_to_delete = node_to_delete.next  # Move to the next node to delete

            # Skip over the deleted nodes
            current.next = node_to_delete
            current = node_to_delete  # Move to the next valid node

def get_input():
    try:
        # Asking user for linked list values
        values = input("Enter numbers for the Linked List (separated by spaces): ").split()
        values = list(map(int, values))  # Convert input to integers
        
        # Asking for how many nodes to skip (m) and delete (n)
        m = int(input("How many nodes to skip (m)? "))
        n = int(input("How many nodes to delete (n)? "))
        
        return values, m, n

    except ValueError:
        print("Oops! Please enter valid integers.")
        return None, None, None

def main():
    values, m, n = get_input()
    
    if values is None or m is None or n is None:
        return  # Exit if input is invalid
    
    linked_list = LinkedList()
    
    # Build the linked list with user input
    for value in values:
        linked_list.append(value)
    
    print("\nOriginal Linked List:")
    linked_list.display()  # Show the list before any deletion
    
    # Now let's apply the deletion logic (skip m, delete n)
    linked_list.delete_after_m_skip_n(m, n)
    
    print("\nModified Linked List:")
    linked_list.display()  # Show the list after modification

if __name__ == "__main__":
    main()
