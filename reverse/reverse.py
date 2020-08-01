class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # def reverse_list(self, node, prev):

    #     '''Reverse a linked list'''

    #     # while the current node exists
    #     while node:

    #         # store the next node
    #         next_node = node.next_node

    #         # set the previous node to the next node
    #         node.next_node = prev
            
    #         # set the current node to the previous node
    #         prev = node

    #         # set the next node to the current node
    #         node = next_node

    #     # if node is None, the previous node is the head!
    #     self.head = prev


    def reverse_list(self, node, prev):

        '''Reverse a linked list recursively'''

        # while the current node exists 
        if node:

            # store the next node
            next_node = node.next_node

            # set the previous node to the next node
            node.next_node = prev

            # run it all through again, with the new root
            self.reverse_list(next_node, node)

        # if node is None
        else:

            # the previous node is the head!
            self.head = prev