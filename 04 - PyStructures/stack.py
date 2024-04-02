history = []

# User actions
history.append("write 'Hello'")
history.append("write 'World'")
history.append("delete 'World'")

# Undo last action
last_action = history.pop()
print(f"Undo: {last_action}")
