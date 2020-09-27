class ChainingNode:
    """
    This class represents a Linked List node used for chaining to resolve
    collisons in a HashMap class.

    Inputs:
        -> key (int): Integer representing the key being hashed into the HashMap
        -> value (int): Integer representing the value being hashed into the HashMap
    """
    def __init__(self, key, value):
        self.key = key
        self.val = value 
        self.next = None 


class HashMap:
    """
    This class represents a HashMap class that accepts integer inputs. All methods
    of a HashMap are supported by this class -> put, remove, get, with dynamic array 
    resizing. 

    HashMaps are built on top of static arrays. This class assumes an initial capacity
    of a static array of 1000, with a load factor equal to 0.75. When the load factor
    is exceeded, dynamic array resizing is done to ensure O(1) TS lookups, removals, and
    additions. 

    Inputs:
        -> k (int): Initial capacity of the static array. Default is 3000.
        -> load_factor (int): Target load factor for the HashMap. Goal is to keep below 0.75. 
    """
    def __init__(self, k=3000, load_factor=0.75):
        self.load_factor = load_factor
        self.static_arr = [None] * k
        self.curr_capacity = 0
    
    def put(self, key, value):
        hash_value = self._hashFunc(key)
        if self.static_arr[hash_value] == None:
            self.static_arr[hash_value] = ChainingNode(key,value)
        else:
            curr_node = self.static_arr[hash_value]
            while curr_node.next and curr_node.key != key:
                curr_node = curr_node.next
            if curr_node.key != key:
                curr_node.next = ChainingNode(key, value)
                self.curr_capacity += 1
                if self.curr_capacity/len(self.static_arr) >= self.load_factor:
                    self._dynamicArrayResizing()
            else:
                curr_node.val = value 
    
    def get(self, key):
        hash_value = self._hashFunc(key)
        if self.static_arr[hash_value] == None:
            return 
        else:
            currNode = self.static_arr[hash_value] 
            while currNode and currNode.key != key:
                currNode = currNode.next
            if not currNode:
                return 
            return currNode.val
    
    def _dynamicArrayResizing(self):
        savedArr = self.static_arr
        self.static_arr = [None] * len(self.static_arr)*2
        for pointer in savedArr:
            if pointer:
                while pointer:
                    currKey = pointer.key 
                    currVal = pointer.val
                    pointer = pointer.next 
                    self.put(currKey, currVal)
    

    def remove(self, key):
        hash_value = self._hashFunc(key)
        if self.static_arr[hash_value] == None:
            return 
        else:
            currNode = self.static_arr[hash_value]
            prevNode = None 
            while currNode and currNode.key != key:
                prevNode =currNode
                currNode = currNode.next 
            if not currNode:
                return  
            self.curr_capacity -= 1
            if not prevNode:
                # you can't just assume that theres nothing else hashed here
                # so we have to set hash_value to currNode.next rather than None outright
                self.static_arr[hash_value] = currNode.next 
                return 
            else:
                prevNode.next = currNode.next 
                currNode = None
                return 
            
    def _hashFunc(self, key):
        # abs() to be able to hash in positive AND negative ints
        # although python does support negative integer indices 
        return abs(key % len(self.static_arr))

