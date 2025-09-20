"""
Need for hashing
----------------------
-To efficiently search in O(1)
-If we want to retrieve in O(1) -> we use map
-Internal of map uses hash table

- Key
- Hash function
- Hash Table

K1, K2 ---> Passed to Hash function ---> Updated in hash table (Index, Value(key))

Usecases
- Image processing, Routing, Network packets, Congestion, etc
- Fraud detection based on hashes of transaction

Eg hash function  = K % size of hash table (where K=key)
K = 2
k%2 = 2 -> Index = 2

We get collision if 2 Hashes are same & its already occupied by some other key

Eg. Sum of ASCII value
Key = ab
Key = ba 

Both will have same hash -> there will be a collision

To handle collision
1. Seperate Chaining
2. Open addressing

Seperate Chaining 
- make each cell point to linked list of records
- the recent nodes will be insert to the first of the chain
- but this uses extra space

Open addressing
- No extra space
- all elements are stored in hash table itself
- 3 types : Linear probing, qudratic probing, double probing

Linear Probing - in case collision -> move to get space (k+1)% size
Qudratic Probing - go to h, h + 1^2, h + 2^2, h + 3 ^2... to find next hash
Double Hashing - h1(k) + i & h2(k) % h


Internals
---------

Hashmap -- random
treemap - natural sorted
linkedhashmap - preserving same order

"""

class HashNode:

    def __init__(self, key, value, next):
        self.key = key 
        self.value = value
        self.next = next

class Map:

    def __init__(self, bucket_size, curr_size):
        self.bucket_size = bucket_size 
        self.curr_size = curr_size 
        self.bucket_array = [None] * self.bucket_size

    
    def __get_bucket_method(self, key):
        # the hashing function implementation
        return int(key) % self.bucket_size

    def add(self, key, value):
        bucket_index = self.get_bucket_index(key)
        # and key exists, find node & update 
        head = self.bucket_array[bucket_index]
        temp = head
        while temp is not None: 
            if temp.key == key:
                temp.value = value
                return 
            temp = temp.next
        # but new key
        # create new node and store
        newnode = HashNode(key, value)
        # replace head with new node 
        newnode.next = head 
        self.bucket_array[bucket_index] = newnode 
        self.curr_size += 1

        # if load factor is more than threshold, 
        # then double the size of bucket

        if (1.0 * self.curr_size) > 0.7:
            self.bucket_array += [None] * self.bucket_size 
            self.bucket_size *= 2 
        

    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        temp = head
        while temp is not None: 
            if temp.key == key:
                return temp.value
            temp = temp.next
        return None    

    def remove(self, key):
        pass 




