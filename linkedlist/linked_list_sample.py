
class LinkedListNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtTheBegging(self, value):
        node = LinkedListNode(value)
        if node is not None:
            node.nextNode = self.head
            self.head = node

    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->")
            currentNode = currentNode.nextNode
        print("None")

    def insertAfter(self, prev_node, new_data):
        _prev_node = self.getNodeByValue(prev_node)
        if _prev_node is None:
            print("There is no such Node in the LinkedList.")
            return
        new_node = LinkedListNode(new_data)
        new_node.nextNode = _prev_node.nextNode
        _prev_node.nextNode = new_node

    def getNodeByValue(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            current_node = current_node.nextNode
        return None


_list = linkedList()
_list.insert("3")
_list.insert("44")
_list.insert("45")

_list.printLinkedList()
print("Before")
_list.insertAfter("44", "4")
_list.insertAfter("3", "4")
print("After")
_list.printLinkedList()

print("\n\n\nBefore")
_list.insertAtTheBegging("666666")
print("After")
_list.printLinkedList()
