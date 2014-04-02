class OrderedList(UnorderedList):
    
    def __init__(self):
        UnorderedList.__init__(self)
        
    def search(self, item):
        """Boolean valued search function."""
        current = self._head
        # search until we find it or fall off the end
        while current != None:
            if current.getData() == item:
                # item has been found
                return True
            else:
                if current.getData() > item:
                    # We’ve passed where the item could be.
                    # Only works for ordered lists.
                    return False
                else:
                    current = current.getNext()
        return False

    def add(self, item):
        """Add an item at the right spot
        in a sorted list."""
        # must keep two pointers marching
        # in synch down the list.
        current = self._head
        previous = None
        while current != None:
            if current.getData() > item:
                # we’ve reached the insertion spot
                break
            else:
                # otherwise, advance both pointers
                previous = current
                current = current.getNext()
        temp = Node(item)
        if previous == None:
            # insert at the start of the list
            temp.setNext(self._head)
            self._head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
