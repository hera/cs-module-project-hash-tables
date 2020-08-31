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
        self.entries = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.
        """
        return len(self.entries)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        counter = 0

        for i in self.entries:
            if i is not None:
                counter += 1
                
                if i.next is not None:
                    counter += 1
        
        return counter / self.capacity


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
        new_entry = HashTableEntry(key, value)
        index = self.hash_index(key)

        # if empty
        if self.entries[index] is None:
            self.entries[index] = new_entry
            return new_entry

        
        current_entry = self.entries[index]

        # check all entries
        while current_entry is not None:
            if current_entry.key == key:
                # override the value
                current_entry.value = value
                return current_entry
            else:
                current_entry = current_entry.next
        
        # add new entry as head
        new_entry.next = self.entries[index]
        self.entries[index] = new_entry

        return self.entries[index]

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Prints a warning if the key is not found.
        """
        warning = f"The key '{key}' is not found."
        index = self.hash_index(key)

        current_entry = self.entries[index]

        if current_entry is None:
            print(warning)
            return

        # if head matches
        if current_entry.key == key:
            self.entries[index] = current_entry.next

        # always keep previous entry
        prev = current_entry

        temp = current_entry.next

        # check all entries
        while temp is not None:
            if temp.key == key:
                prev.next = temp.next
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
        current_entry = self.entries[index]

        if current_entry is None:
            return None
        else:
            # check all entries in a linked list
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
        pass



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
