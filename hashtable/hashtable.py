class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity=MIN_CAPACITY):
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY

        self.capacity = capacity
        self.storage = [None] * capacity
        self.storage_counter = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        return self.storage_counter / self.capacity
    
    def check_resize(self):
        """
        Check if storage resize is needed
        """
        factor = self.get_load_factor()

        if factor >= 0.7:
            self.resize(self.capacity * 2)
        elif factor <= 0.2:
            self.resize(MIN_CAPACITY)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        pass


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        """

        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        """

        self.check_resize()

        new_entry = HashTableEntry(key, value)
        index = self.hash_index(key)

        # if empty
        if self.storage[index] is None:
            self.storage[index] = new_entry
            self.storage_counter += 1
            return new_entry

        
        current_entry = self.storage[index]

        # check all storage
        while current_entry is not None:
            if current_entry.key == key:
                # override the value
                current_entry.value = value
                return current_entry
            else:
                current_entry = current_entry.next
        
        # add new entry as head
        new_entry.next = self.storage[index]
        self.storage[index] = new_entry
        self.storage_counter += 1

        return self.storage[index]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Prints a warning if the key is not found.
        """

        self.check_resize()

        warning = f"The key '{key}' is not found."
        index = self.hash_index(key)

        current_entry = self.storage[index]

        if current_entry is None:
            print(warning)
            return

        # if head matches
        if current_entry.key == key:
            self.storage[index] = current_entry.next
            self.storage_counter -= 1

        # always keep previous entry
        prev = current_entry

        temp = current_entry.next

        # check all storage
        while temp is not None:
            if temp.key == key:
                prev.next = temp.next
                self.storage_counter -= 1
                return temp.value
            else:
                temp = temp.next

        # not found
        print(warning)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        index = self.hash_index(key)
        current_entry = self.storage[index]

        if current_entry is None:
            return None
        else:
            # check all storage in a linked list
            while current_entry is not None:
                # if matches
                if current_entry.key == key:
                    return current_entry.value
                else:
                    # otherwise go to the next one
                    current_entry = current_entry.next
        
        return None
                
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        """

        self.capacity = new_capacity

        new_storage = [None] * new_capacity
        new_storage_counter = 0

        for entry in self.storage:
            current_entry = entry

            while current_entry is not None:
                # generate a new index
                new_index = self.hash_index(current_entry.key)

                # create a new entry
                new_entry = HashTableEntry(current_entry.key, current_entry.value)

                # Save it in new_storage

                # If position is empty
                if new_storage[new_index] is None:
                    new_storage[new_index] = new_entry
                    new_storage_counter += 1
                else:
                    # for each of the elements in the linked list
                    # check if override is needed
                    last = new_storage[new_index]

                    while last is not None:
                        if last.key == current_entry.key:
                            last.value = current_entry.value
                            break
                        else:
                            last = last.next
                    
                    # nothing matched, so add the new entry as head
                    new_entry.next = new_storage[new_index]
                    new_storage[new_index] = new_entry
                    new_storage_counter += 1
                
                # proceed to the next entry in the linked list
                current_entry = current_entry.next
        
        # update storage

        self.storage = new_storage
        self.storage_counter = new_storage_counter


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
