from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            num = self.dict[key]
            self.dict.pop(key)
            self.dict[key] = num
            return num
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # num = self.dict[key]
            self.dict.pop(key)
            self.dict[key] = value

        else:
            if len(self.dict) >= self.size:
                # print("exceed")
                self.dict.popitem(last=False)
            # print(key)
            self.dict[key] = value

    def toString(self):
        for i in self.dict.items():
            print(i)


# cache = LRUCache(2)
# cache.put(2, 6)
# print(cache.get(1))
# cache.put(1, 5)
# cache.put(1, 3)
# print(cache.get(1))
# # cache.put(3, 3)
# # cache.toString()
# print(cache.get(2))
# cache.toString()
cache = LRUCache(3)

cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)

print(cache.get(1))  # expect 1
print(cache.get(2))  # expect 2
print(cache.get(4))  # expect -1

cache.put(4, 4)

print(cache.get(1))  # expect 1
print(cache.get(2))  # expect 2
print(cache.get(3))  # expect -1
print(cache.get(4))  # expect 4

print(cache.get(2))  # expect 2 / 2 -> 4 -> 1

cache.put(1, 8)  # 1 -> 2 -> 4
cache.put(3, 7)  # 3 -> 1 -> 2

print(cache.get(1))  # expect 8
print(cache.get(2))  # expect 2
print(cache.get(3))  # expect 7
print(cache.get(4))  # expect -1
print(cache.get(5))  # expect -1

print(cache.get(2))  # expect 2
print(cache.get(3))  # expect 7
print(cache.get(4))  # expect -1

cache.put(1, 9)
cache.put(6, 6)

print(cache.get(1))  # expect 9
print(cache.get(2))  # expect -1
print(cache.get(3))  # expect 7
print(cache.get(4))  # expect -1
print(cache.get(5))  # expect -1
print(cache.get(6))  # expect 6
