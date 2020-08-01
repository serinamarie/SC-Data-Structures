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

    def reverse_list(self, node, prev):
        # the head is 5, in the input is head,
        # the prev is None
        # none 5 4 3 2 1
        

        # if there is a next node 
        while node:

            # make the next node the new node 
            #1
            next_node = node.next_node

            # set the node's (5) next to  
            # None is the current's next node
            #3 is the next node.next_node
            node.next_node = prev
            # 2 is the prev
            prev = node
            # 1 is the node
            node = next_node
        self.head = prev
            


        # if node.next_node:
        #     node.next_node = prev
        #     return self.reverse_list(node.next_node, node)

        # else:
            # self.head = current
        
        # if node.next_node is None:
        #     self.head = node
        #     return self.head
        # else: 
        #     current = node
        #     node.next_node = prev
            
        #     if current.next_node:
        #         self.reverse_list(current.next_node, node)

        #     else:
        #         self.head = current




        # node = self.head

        # if node.next_node is not None:
        #     temp = node.next_node
        #     node.next = prev
        #     self.reverse_list(temp, node)
        # else:
        #     return node 




        # cur_node = self.head
        # next_node = cur_node.next_node

        # cur_node.set_next(None)
        # self.head = cur_node
        # while next_node is not None:
        #     prev_node = cur_node
        #     cur_node = next_node
        #     next_node = cur_node.get_next()
        #     cur_node.set_next(prev_node)


        
        


       








        # while node.next_node is not None:

    
        # if node.next_node:
        #     self.reverse_list(node.next_node, node)


        # if node.next_node:
        #     temp = node.next_node
        #     node.next_node = prev
        #     return reverse_list(temp, node)
        # else:
        #     return node.get_value()

        #     # the 2 is now after the 1
        #     node.next_node = prev
        #     self.head = node


        # new_root = self.reverse_list(node.next_node, node)
        # node.next_node = prev
        # return new_root

        
        # # node.prev = 1

        


        


        

        
