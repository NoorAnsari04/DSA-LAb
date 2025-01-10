class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# creating a LinkedList        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        if not self.head:
            print("The linked list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")
        
    def delete_nodes_after_m(self, m, n):
        if m < 0 or n < 0:
            print("m and n cannot be negative numbers")
            return
        
        current = self.head
        while current:
            # Skip m nodes
            for _ in range(m):
                if current is None or current.next is None:
                    return
                current = current.next
            
            # Delete n nodes
            temp = current.next
            for _ in range(n):
                if temp is None:
                    break
                temp = temp.next
            
            # Link the current node to the (m + n + 1)-th node
            current.next = temp
            current = temp
        
def user_input():
    try:
        # Get LinkedList from the user
        values = input("Enter the values for the LinkedList:").split()
        values = list(map(int, values))
        
        # Get values for m and n
        m = int(input("Enter the number of nodes to skip (m): "))
        n = int(input("Enter the number of nodes to delete (n): "))
        
        return values, m, n
        
    except ValueError:
        print("Invalid Input")
        return None, None, None
        
def main():
    values, m, n = user_input()
    
    if values is None or m is None or n is None:
        return
                
    linked_list = LinkedList()            
    for value in values:
        linked_list.append(value)
        
    print("Original LinkedList:")
    linked_list.display()
    
    # Apply delete operation
    linked_list.delete_nodes_after_m(m, n)
    print("\nChanged LinkedList:")
    linked_list.display()
    
if __name__ == "__main__":
    main()
