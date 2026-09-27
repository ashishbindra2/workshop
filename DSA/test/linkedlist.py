class Node:
    """
    creating a node
    """
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    current = head
    while current:
            print(current.data,"->",end=" ")
            current = current.next
    print("null")

def insert_new_node_at_begining(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insert_at_end(head,val):
    new_node = Node(val)
    
    if head is None:
         return new_node
    current = head
    while current.next is not None:
            current = current.next
    current.next = new_node
    return head

def at_mid(head,val,pos):
    if pos <1:
        return head
    
    if pos ==1:
        return insert_new_node_at_begining(head, val)
    current = head
    new_node = Node(val)
    for i in range(1,pos):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    return head

if __name__ == "__main__":
    head =None
    head = Node(1)
    # head.next = Node(2)
    traverse(head)

    # head = insert_new_node_at_begining(head, 9)
    # traverse(head)

    # head = insert_at_end(head, 6)
    traverse(head)

    head = at_mid(head,3,1)
    traverse(head)

    # head = at_mid(head,5,4)
    # traverse(head)

    # head = at_mid(head,4,4)
    # traverse(head)
