class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None

    # used to print all linked list
    def list_print(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    # used to insert a new node at beginning of linked list
    def insert_at_start(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_idx(self, val, idx):
        new_node = Node(val)
        curr_node = self.head
        possition = 0

        if possition == idx:
            self.insert_at_start(val)
        else:
            while(curr_node.next != None and possition + 1 != idx):
                possition += 1
                curr_node = curr_node.next
            
            # This if statement ensures that not adding new node at end of the list while getting out of range value of idx
            if possition < idx-1:
                print("Index out of range")
                return
            elif curr_node != None:
                new_node.next = curr_node.next
                curr_node.next = new_node


l = SLL()

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

l.head = e1
l.head.next = e2
e2.next = e3

l.insert_at_start(10)
l.insert_at_idx(22, 3)

l.list_print()