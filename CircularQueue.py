class CircularQueue:
    def __init__(self, size):
        self.maxSize = size
        self.queue = [0] * size
        self.front = 0
        self.rear = -1
        self.currentSize = 0

    def isEmpty(self):
        return self.currentSize == 0

    def isFull(self):
        return self.currentSize == self.maxSize

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.maxSize  # Circular increment of rear
        self.queue[self.rear] = item
        self.currentSize += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return -1  # or throw an exception
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.maxSize  # Circular increment of front
        self.currentSize -= 1
        return item

    def peek(self):
        if self.isEmpty():
            print("Queue is empty. Cannot peek.")
            return -1  # or throw an exception
        return self.queue[self.front]


if __name__ == "__main__":
    queue = CircularQueue(5)  # Create a queue with a maximum size of 5

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Front element:", queue.peek())

    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())

    queue.enqueue(4)
    queue.enqueue(5)

    print("Front element:", queue.peek())

    while not queue.isEmpty():
        print("Dequeued:", queue.dequeue())
