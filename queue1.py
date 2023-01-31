class Queue:
    def __init__(self):
        self.queue = list()

    def addend(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    def addtobig(self, dataval):
        length = len(self.queue)
        if dataval not in self.queue:
            self.queue.insert(length, dataval)
            return True
        return False

    def size(self):
        return len(self.queue)

    def pop(self):
        self.queue.pop()

    def popend(self):
        self.queue.pop(0)

    def show(self):
        return self.queue


TheQueue = Queue()
TheQueue.addend('Mon')
TheQueue.addend('Tue')
TheQueue.addend('Wed')
print(TheQueue.show())
print(TheQueue.size())
TheQueue.addtobig('Fri')
print(TheQueue.show())
TheQueue.pop()
print(TheQueue.show())
TheQueue.popend()
print(TheQueue.show())
