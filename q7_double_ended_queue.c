/*
 * Question 7: Operations on a double ended queue (deque) in C
 * (a) Front insertion  (b) Rear insertion
 * (c) Front deletion   (d) Rear deletion
 * Implemented as a circular array.
 */
#include <stdio.h>

#define SIZE 5

int deque[SIZE];
int front = -1, rear = -1;

int isFull(void)  { return (front == 0 && rear == SIZE - 1) || (front == rear + 1); }
int isEmpty(void) { return front == -1; }

/* (a) Front insertion */
void insertFront(int value) {
    if (isFull()) {
        printf("Deque OVERFLOW\n");
        return;
    }
    if (isEmpty())
        front = rear = 0;
    else if (front == 0)
        front = SIZE - 1;
    else
        front--;
    deque[front] = value;
    printf("Inserted %d at front\n", value);
}

/* (b) Rear insertion */
void insertRear(int value) {
    if (isFull()) {
        printf("Deque OVERFLOW\n");
        return;
    }
    if (isEmpty())
        front = rear = 0;
    else if (rear == SIZE - 1)
        rear = 0;
    else
        rear++;
    deque[rear] = value;
    printf("Inserted %d at rear\n", value);
}

/* (c) Front deletion */
void deleteFront(void) {
    if (isEmpty()) {
        printf("Deque UNDERFLOW\n");
        return;
    }
    printf("Deleted %d from front\n", deque[front]);
    if (front == rear)
        front = rear = -1;
    else if (front == SIZE - 1)
        front = 0;
    else
        front++;
}

/* (d) Rear deletion */
void deleteRear(void) {
    if (isEmpty()) {
        printf("Deque UNDERFLOW\n");
        return;
    }
    printf("Deleted %d from rear\n", deque[rear]);
    if (front == rear)
        front = rear = -1;
    else if (rear == 0)
        rear = SIZE - 1;
    else
        rear--;
}

void display(void) {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }
    printf("Deque (front -> rear): ");
    int i = front;
    while (1) {
        printf("%d ", deque[i]);
        if (i == rear) break;
        i = (i + 1) % SIZE;
    }
    printf("\n");
}

int main(void) {
    int choice, value;
    do {
        printf("\n--- DOUBLE ENDED QUEUE ---\n");
        printf("1. Insert at front\n2. Insert at rear\n");
        printf("3. Delete from front\n4. Delete from rear\n");
        printf("5. Display\n6. Exit\n");
        printf("Enter choice: ");
        if (scanf("%d", &choice) != 1) break;
        switch (choice) {
            case 1:
                printf("Enter value: ");
                scanf("%d", &value);
                insertFront(value);
                break;
            case 2:
                printf("Enter value: ");
                scanf("%d", &value);
                insertRear(value);
                break;
            case 3: deleteFront(); break;
            case 4: deleteRear(); break;
            case 5: display(); break;
            case 6: printf("Goodbye!\n"); break;
            default: printf("Invalid choice\n");
        }
    } while (choice != 6);
    return 0;
}
