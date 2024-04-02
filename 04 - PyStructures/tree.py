class FileNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, node):
        self.children.append(node)


root = FileNode("Root")
folder1 = FileNode("Folder1")
file1 = FileNode("File1")

root.add_child(folder1)
folder1.add_child(file1)
