class MyHashMap:

    def __init__(self, capacity = 16):
        self.MAX_SIZE = 10000
        self.bucket = [[] for _ in range(self.MAX_SIZE)]
        
    def getBucketIndex(self, key) -> int:
        return hash(key) % self.MAX_SIZE

    def put(self, key: int, value: int) -> None:
        index = self.getBucketIndex(key)
        for i, (k, v) in enumerate(self.bucket[index]):
            # if key already exist, replace it
            if k == key:
                self.bucket[index][i] = [key, value]
                return
        # otherwise, append to the bucket
        self.bucket[index].append([key, value])
    

    def get(self, key: int) -> int:
        index = self.getBucketIndex(key)
        for (k,v) in self.bucket[index]:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.getBucketIndex(key)
        for i, (k,v) in enumerate(self.bucket[index]):
            if k == key:
                self.bucket[index][i] = self.bucket[index][-1]
                self.bucket[index].pop()
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)