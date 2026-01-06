from typing import DefaultDict


class TimeMap:
    def __init__(self):
        self.dict = DefaultDict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dict:
            self.dict[key].append([value, timestamp])
        else:
            self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        items = self.dict[key]
        left = 0
        right = len(items) - 1
        prev_value, prev_time = items[0]
        while left <= right:
            mid = (left + right) // 2
            value, time = items[mid]
            if time == timestamp:
                return value
            if time > timestamp:
                right = mid - 1
            else:
                prev_value = value
                prev_time = time
                left = mid + 1
        if prev_time != 0 and prev_time <= timestamp:
            return prev_value
        else:
            return ""

    def print(self):
        for key, value in self.dict["alice"]:
            print(f"{key} {value}")
            # for i, j in value:
            #     print(f"key {key} {i} {j}")


time = TimeMap()
# time.set("alice", "happy", 1)
# print(time.get("alice", 1))
# print(time.get("alice", 2))
# time.set("alice", "sad", 3)
# print(time.get("alice", 3))
# # time.print()
time.set("test", "one", 10)
time.set("test", "two", 20)
time.set("test", "three", 30)

print(time.get("test", 15))
print(time.get("test", 25))
print(time.get("test", 35))
# "get", ["test", 15], "get", ["test", 25], "get", ["test", 35]]
