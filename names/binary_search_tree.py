class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):

        '''Insert the given value into the tree'''

        # if the input is less than the current value
        if value < self.value:

            # if there is no left child
            if not self.left:

                # insert it!
                self.left = BSTNode(value)
            
            # if there is already a left child
            else:

                # repeat the process
                self.left.insert(value)

        # if the input is more than or equal to the current value
        elif value >= self.value:

            # if there is no right child
            if not self.right:

                # the input is now the right child!
                self.right = BSTNode(value)

            # if there is already a right child
            else:

                # repeat the process
                self.right.insert(value)


    def contains(self, target):

        """Returns true if the tree contains the value.
        False if it does not.
        """

        # if the input is the current value        
        if target == self.value:

            # it exists in the BST!
            return True

        # otherwise if the the input is less than the current value
        elif target < self.value:

            # if there is no left child
            if not self.left:

                # it ain't in this tree
                return False

            # if there is a left child
            else:

                # recursion (the left child is the new tree root, see if target is in it)
                return self.left.contains(target)

        # otherwise if the input is greater than or equal to the target
        elif target >= self.value:

            # if there is no right child
            if not self.right:

                # it ain't in this tree
                return False

            # if there is a right child
            else:

                # recursion (the right child is the new tree root, see if target is in it)
                return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):

        # the current value is the max, for now
        current_max = self.value

        # if there's no value larger than the current value
        if not self.right:

            # than this value is the biggest :)
            return current_max

        # if there is a value larger than the current value
        elif self.right:

            # set the root of the tree to the right child and run 
            # the new current_max through the function
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        # call the function on the input value
        fn(self.value)

        # if there is a left child
        if self.left:

            # run the function through again 
            # with the left child as the root of the tree
            self.left.for_each(fn)

        # if there is a right child
        if self.right:

            # run the function through again 
            # with the right child as the root of the tree
            self.right.for_each(fn)
            
    def delete(self, value):
        # unfinished/untested
        if value == self.value:
            # if no children
            if not self.left and not self.right:
                self.value = None
            # if two children
            elif self.left and self.right:
                self.value = self.right

            # if one child
            elif self.left and not self.right:
                self.value = self.left
            

    # Part 2 -----------------------


    def in_order_print(self):

        '''Print all the values in order from low to high
        Use a recursive, depth first traversal
        
        '''
        # if there is a tree
        if self:

            # if there is a left child
            if self.left:
                # make left child root of tree
                self.left.in_order_print()

            # print the current root
            print(self.value)

            # if there is a right child
            if self.right:

                # make the right child root of tree
                return self.right.in_order_print()


    def bft_print(self):
  
        '''Print the value of every node, starting with the given node,
        in an iterative breadth first traversal
        '''
        # instantiate a Queue
        q = Queue()
        
        # insert the value
        q.enqueue(self)

        # while length of q is greater than 0
        while q.size > 0: 

            # pop off the top
            front = q.dequeue()

            # print it
            print(front.value)

            # if there is a left child
            if front.left:

                # add left child to queue
                q.enqueue(front.left)

            # if there is a right child
            if front.right:

                # add right child to queue
                q.enqueue(front.right)


    def dft_print(self):

        '''Print the value of every node, starting with the given node,
        in an iterative depth first traversal'''

        # a maze is a good example
        # So, a preorder traversal?! we'll try that
        
        # if a tree exists
        if self:

            # print the current value (as it's the first traversal)
            print(self.value)

        # if there is a left child
        if self.left:

            # re-run function with left child as root of tree
            self.left.dft_print()

        # if there is a right child
        if self.right:

            # re-run function with right child as root of tree
            self.right.dft_print()


    # Stretch Goals -------------------------
    # Note: Research may be required

    
    def pre_order_dft(self):

        # Print Pre-order recursive DFT
        # Oops, already did this in the function above
        # But they both have the same output so I'll c/p this
        
        if self:

            # print the current value (as it's the first traversal)
            print(self.value)

        # if there is a left child
        if self.left:

            # re-run function with left child as root of tree
            self.left.pre_order_dft()

        # if there is a right child
        if self.right:

            # re-run function with right child as root of tree
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):

        # need to sleep on this one 
        pass
