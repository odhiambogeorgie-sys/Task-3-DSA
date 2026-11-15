"""
CCS 2214 - Task 3
Question 5: Program to perform enqueue and dequeue in a Queue
(linear queue implemented using a fixed-size list)
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value):
        if self.count == self.capacity:
            print(f"Queue OVERFLOW. Cannot insert {value}")
            return
        self.rear += 1
        self.items[self.rear] = value
        self.count += 1
        print(f"Enqueued {value}")

    def dequeue(self):
        if self.count == 0:
            print("Queue UNDERFLOW. Queue is empty")
            return None
        value = self.items[self.front]
        self.front += 1
        self.count -= 1
        if self.count == 0:          # reset when empty
            self.front, self.rear = 0, -1
        print(f"Dequeued {value}")
        return value

    def display(self):
        if self.count == 0:
            print("Queue is empty")
            return
        print("Queue (front -> rear):", *self.items[self.front:self.rear + 1])


def main():
    q = Queue(5)
    while True:
        print("\n--- QUEUE ---")
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
