class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)


# Create a new LinkedList instance for our music playlist
playlist = LinkedList()

# Add some songs to the playlist
playlist.append("Song 1: Hello World")
playlist.append("Song 2: Goodbye Moon")
playlist.append("Song 3: Python's Serenade")

# Display the playlist
print("Your Music Playlist:")
playlist.display()
# Expected output:
# Your Music Playlist:
# Song 1: Hello World
# Song 2: Goodbye Moon
# Song 3: Python's Serenade
