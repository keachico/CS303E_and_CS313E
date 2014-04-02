class UnorderedList:
    """A linked list in which the items are unordered."""
    def __init__(self):
            """Create an empty list of no items and
                length 0."""
            self._head = None
            self._length = 0
            
    def isEmpty(self):
        return not self._head

    def __str__(self):
        """Adding all items to the printstring requires
            traversing the list."""
        output = "[ "
        ptr = self._head
        while ptr != None:
            output += str(ptr.getData()) + " "
            ptr = ptr.getNext()
        return output + "]"

    # Continues the UnorderedList class
    
    def get(self, index):
        """Fetch the item at the indexed position."""
        # Is the index within bounds?
        if index < 0 or index >= self._length:
            print ("Index out of range.")
            return None
        # Count down the list until you reach the
        # right node.
        cursor = self._head
        for i in range(index):
            cursor = cursor.getNext()
        return cursor.getData()
    
    def add(self, item):
        # Add an item to the front of the list.
        temp = Node(item)
        temp.setNext( self._head )
        self._head = temp
        self._length += 1

    def remove(self, item):
        """Remove first occurrence of item, if any."""
        current = self._head
        previous = None
        found = False
        while not found and current != None:
            if current.getData() == item:
                self._length -= 1
                found = True
            else:
                previous = current
                current = current.getNext()
        if current == None:
            # item is not in the list
            return
        elif previous == None:
            # item is at head of the list
            self._head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def search(self, item):
        """Return a boolean indicating whether
            item is in the list."""
        
        current = self._head
        # Search to find item or fall off the end.
        while current != None:
            if current.getData() == item:
                return True
            else:
                current = current.getNext()
        # If you reach the end of the list.
        return False
