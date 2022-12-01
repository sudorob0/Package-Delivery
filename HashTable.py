# HashTable class using chaining.
class ChainingHashTable:
    def __init__(self, initial_capacity=16):
        """Creates a hash table with chaining capability"""
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """Inserts a value into a bucket"""
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        """Searches for a value in the hash table"""
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    def remove(self, key):
        """Removes a value from the hash table"""
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])
