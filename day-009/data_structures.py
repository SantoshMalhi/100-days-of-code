from collections import deque

def list_example():
    print("List Example")
    fruits = ["apple", "banana", "cherry"]
    print("Initial list:", fruits)
    
    # Adding elements
    fruits.append("orange")
    print("After append:", fruits)
    
    # Accessing elements
    print("Second element:", fruits[1])
    
    # Removing elements
    fruits.remove("banana")
    print("After removal:", fruits)
    print()

def stack_example():
    print("Stack Example")
    stack = []
    
    # Adding elements (push operation)
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print("Stack after push operations:", stack)
    
    # Removing elements (pop operation)
    print("Pop operation result:", stack.pop())
    print("Stack after pop operation:", stack)
    print("Pop operation result:", stack.pop())
    print("Stack after pop operation:", stack)
    print()

def queue_example():
    print("Queue Example")
    queue = deque()
    
    # Adding elements (enqueue operation)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("Queue after enqueue operations:", queue)
    
    # Removing elements (dequeue operation)
    print("Dequeue operation result:", queue.popleft())
    print("Queue after dequeue operation:", queue)
    print("Dequeue operation result:", queue.popleft())
    print("Queue after dequeue operation:", queue)
    print()

if __name__ == "__main__":
    list_example()
    stack_example()
    queue_example()
