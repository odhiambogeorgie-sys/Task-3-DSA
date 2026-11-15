"""
CCS 2214 - Data Structure and Algorithms | Task 3
Question 1: Circular queue implementation in Python

Disadvantage of a linear queue: once rear reaches the last index, no more
insertions are possible even if front has moved forward and freed space at
the start. A circular queue wraps around using modulo arithmetic so freed
slots are reused.
"""


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print(f"Queue is FULL. Cannot insert {value}")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Inserted {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is EMPTY. Nothing to delete")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:      # last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted {value}")
        return value

    def display(self):
        if self.is_empty():
            print("Queue is EMPTY")
            return
        items = []
        i = self.front
        while True:
            items.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("Queue:", *items)


def main():
    q = CircularQueue(5)
    while True:
        print("\n--- CIRCULAR QUEUE ---")
        print("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            q.enqueue(int(input("Enter value: ")))
        elif choice == "2":
            q.dequeue()
        elif choice == "3":
            q.display()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
