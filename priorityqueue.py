class CustomTask:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        # 自定义比较逻辑：按 name 排序
        return self.name < other.name

from queue import PriorityQueue

pq = PriorityQueue()

# 插入自定义对象
pq.put(CustomTask(1, 'task3'))
pq.put(CustomTask(2, 'task1'))
pq.put(CustomTask(3, 'task2'))

while not pq.empty():
    task = pq.get()
    print(f"priority={task.priority}, name={task.name}")