# 写一个有状态记录功能的哈希表，比如有100个状态，每次调用takeshot功能会记录一个新状态。
# 实现get put takeshot init 功能，可以调用python自己的字典、list等数据结构

# 比如说第1次截图id是1，第2次截图id是2，那我就在字典里面存 KEY1->[[1,VALUE1],[2,VALUE1]] 这样，
# 然后如果在第二次截图后删除的话，我就删除成 KEY1->[[1,VALUE1],[2,]]，这样get的时候发现value是空的就会返回获取不到
# 主要他说截图的次数小于100，我想着就大不了就在数组里存100个[1,VALUE1] 这样的元素

class StatefulHashMap:
    def __init__(self):
        self.data = {}
        self.cur_snap_id = 0
        self.max_snapshots = 100
    def put(self,key,value):
        if key not in self.data:
            self.data[key] = [None for i in range(self.max_snapshots)]
        self.data[key][self.cur_snap_id] = value
    
    def get(self,key):
        if key not in self.data:
            raise KeyError("not exist this key")
        val = self.data[key][self.cur_snap_id]
        return val if val is not None else None
    
    def takeshot(self):
        if self.cur_snap_id + 1 > self.max_snapshots:
            return ValueError("snapshots overflow")
        self.cur_snap_id += 1
        for k in self.data:
            self.data[k][self.cur_snap_id] = self.data[k][self.cur_snap_id -1]

    def delete(self,key):
        if key in self.data:
            self.data[key][self.cur_snap_id] = None
        
        


if __name__ == "__main__":
    table = StatefulHashMap()
    
    # Test basic put and get
    table.put("key1", "value1")
    print(table.get("key1"))  # Should print: value1
    
    # Test snapshot functionality
    table.takeshot()  # snapshot 1
    table.put("key2", "value2")
    print(table.get("key1"))  # Should print: value1
    print(table.get("key2"))  # Should print: value2
    
    # Test delete
    table.delete("key1")
    print(table.get("key1"))  # Should print: None
    print(table.get("key2"))  # Should print: value2
    
    # Test multiple snapshots
    table.takeshot()  # snapshot 2
    table.put("key1", "value1_new")
    print(table.get("key1"))  # Should print: value1_new
    
    # Test key error
    try:
        print(table.get("nonexistent_key"))
    except KeyError as e:
        print(f"Expected error: {e}")  # Should print error message
