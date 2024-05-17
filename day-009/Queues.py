from collections import deque

# Queue example
queue = deque()

# Adding elements (enqueue operation)
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])

# Removing elements (dequeue operation)
print(queue.popleft())  # Output: 1
print(queue)  # Output: deque([2, 3])
print(queue.popleft())  # Output: 2
print(queue)  # Output: deque([3])
