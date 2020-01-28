class Node:
    def __init__(self, data_to_set, priority_to_set):
        self.data=data_to_set
        self.priority=priority_to_set


class priority_deque:
    def __init__(self):
        self.nodes=list()
        self.size=0

    def  enqueue(self, data, priority):
        self.size=self.size+1
        self.nodes.append(Node(data, priority))

    def print_deque(self):
        for i in self.nodes:
            print("data: "+ str(i.data)+"\npriority: "+ str(i.priority) + "\n")

    def dequeue(self):
        max_priority=self.nodes[0].priority
        index_of_max_priority=0
        for i in range(len(self.nodes)):
            if self.nodes[i].priority > max_priority:
                index_of_max_priority = i
        res = self.nodes[index_of_max_priority]
        del self.nodes[index_of_max_priority]
        return res


pd = priority_deque()
pd.enqueue(1,100)
pd.enqueue(2,30)
pd.enqueue(3,50)
pd.enqueue(4,30)
pd.print_deque()
print(pd.dequeue().data)
print(pd.dequeue().data)


