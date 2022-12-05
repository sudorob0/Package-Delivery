# HashTable class using chaining.

class ChainingHashTable:
    def __init__(self, initial_capacity=16):
        """Creates a hash table with chaining capability"""
        # initiate list
        self.table = []
        # add empty lists inside of parent list
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """Inserts a value into a bucket"""
        # assign a bucket index based of the modulus of the key
        bucket = hash(key) % len(self.table)
        # save the bucket to a variable
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # save the key value to a list
        key_value = [key, item]
        # add list to the bucket
        bucket_list.append(key_value)
        return True

    def lookup(self, key):
        """Searches for a value in the hash table"""
        # get the bucket index base of the modulus of the key
        bucket = hash(key) % len(self.table)
        # save the bucket to a variable
        bucket_list = self.table[bucket]
        # Iterate through the list to find the key
        for key_value in bucket_list:
            if key_value[0] == key:
                # return object
                return key_value[1]
        return None

    def remove(self, key):
        """Removes a value from the hash table"""
        # get the bucket index base of the modulus of the key
        bucket = hash(key) % len(self.table)
        # save the bucket to a variable
        bucket_list = self.table[bucket]
        # Iterate through the list to find the key
        for key_value in bucket_list:
            if key_value[0] == key:
                #remove the key, value pair
                bucket_list.remove([key_value[0], key_value[1]])

# (Lysecky, R., & Vahid, F. (2018, June). C950: Data Structures and Algorithms II. zyBooks.
# Retrieved November 22, 2022, from  https://learn.zybooks.com/zybook/WGUC950AY20182019/.
