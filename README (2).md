# CCS 2214 – Data Structure and Algorithms: Task 3

**Institution:** Multimedia University of Kenya
**Faculty:** Faculty of Computing and Information Technology
**Unit:** CCS 2214 – Data Structure and Algorithms
**Student:** Odhiambo George Otieno
**Registration No.:** CIT-227-082/2025
**Programme:** Software Engineering
**Due date:** Sunday, 15th November 2026

## About

This repository contains the programming solutions for Task 3. All programs are written in **Python**, except Question 7, which is written in **C** as the question requires. The theory questions (Q2, Q3 and Q8) are answered in the submitted document.

## Repository structure

```
ccs2214-task3/
├── q1_circular_queue.py
├── q4_recursion.py
├── q5_queue.py
├── q6_sparse_matrix.py
├── q7_double_ended_queue.c
└── README.md
```

## Questions and solutions

| Question | Description | File | Language |
|----------|-------------|------|----------|
| Q1 | Circular queue implementation (and disadvantages of a linear queue) | `q1_circular_queue.py` | Python |
| Q4(a) | Recursive sum of the first N natural numbers | `q4_recursion.py` | Python |
| Q4(b) | Recursive factorial of a number | `q4_recursion.py` | Python |
| Q4(c) | Recursive Nth term of the Fibonacci series | `q4_recursion.py` | Python |
| Q4(d) | Recursive generation of N terms of the Fibonacci series | `q4_recursion.py` | Python |
| Q5 | Enqueue and dequeue operations in a queue | `q5_queue.py` | Python |
| Q6 | Sparse matrix representation using arrays (triplet form) | `q6_sparse_matrix.py` | Python |
| Q7 | Double ended queue: front/rear insertion and deletion | `q7_double_ended_queue.c` | C |

## Requirements

- Python 3.8 or later
- GCC (or any C compiler) for Question 7

## How to run

### Python programs (Q1, Q4, Q5, Q6)

```bash
python q1_circular_queue.py
python q4_recursion.py
python q5_queue.py
python q6_sparse_matrix.py
```

### C program (Q7)

```bash
gcc q7_double_ended_queue.c -o q7
./q7          # Windows: q7.exe
```

## Program notes

**Q1 – Circular queue.** A linear queue cannot reuse the space freed at the front once `rear` reaches the last index. The circular queue fixes this by wrapping indices with modulo arithmetic. The program offers a menu to enqueue, dequeue and display.

**Q4 – Recursion.** Four recursive functions with clear base cases. The program prompts for input for each part in turn.

**Q5 – Queue.** An array-based linear queue with overflow and underflow checks.

**Q6 – Sparse matrix.** Only non-zero elements are stored as `(row, column, value)` triplets. The first triplet holds the matrix dimensions and the count of non-zero elements.

**Q7 – Double ended queue.** A circular-array deque with four operations: `insertFront`, `insertRear`, `deleteFront` and `deleteRear`, plus a menu-driven `main`.

## Sample output (Q6)

Input matrix:

```
0 0 5
0 8 0
0 0 0
```

Output:

```
Row  Col  Value
3    3    2
0    2    5
1    1    8
```
