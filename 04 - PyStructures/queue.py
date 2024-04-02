from collections import deque

print_queue = deque()

print_queue.appendleft("Document1")
print_queue.appendleft("Document2")
print_queue.appendleft("Photo1")

next_job = print_queue.pop()
print(f"Printing: {next_job}")
