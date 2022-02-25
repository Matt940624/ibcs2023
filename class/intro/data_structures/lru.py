class LRUCache:
    def __init__(self, capcity: int):
        self.dict = {}
        self.max_cap = capcity

    def get(self, key: int) -> int:
        dict = self.dict

        if key in dict.keys():
            value = dict.get(key)
            del dict[key]
            dict[key] = value
            print(dict)
            return value

        else:
            print(dict)
            return -1

    def put(self, key: int, value: int) -> None:
        dict = self.dict
        cap = self.max_cap

        if len(dict.keys()) < cap:
            if key in dict.keys():
                dict[key] = value
                del dict[key]
                dict[key] = value
                print(dict)
            else:
                dict[key] = value
                del dict[key]
                dict[key] = value
                print(dict)
        else:
            first = list(dict.keys())[0]
            del dict[first]
            dict[key] = value
            print(dict)


# Your LRUCache object will be instantiated and called as such:


obj = LRUCache(3)


obj.put(1, 4)
obj.put(2, 5)
obj.put(3, 6)
obj.put(4, 7)


param_1 = obj.get(2)
param_2 = obj.get(3)
param_3 = obj.get(5)

print(param_1)
print(param_2)
print(param_3)
