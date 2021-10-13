#Singly Linked List
#Author:  Thomas S
#Date: 14 Sept 2021

#Create Class Node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

#Create Class Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    #Print Linked LinkedList
    def printList(self):
        currNode = self.head

        while currNode is not None:
            print(currNode.data, end= " | ")
            currNode = currNode.next
        print("\n\n")
    #Insert At Front
    def insertAtFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    #Insert At Back
    def insertAtBack(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        currNode = self.head

        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = newNode



#Create LinkedList Object
linkedList = LinkedList()

#Create 1st Node of List
linkedList.head = Node("Ferrari")

#Create Some More Nodes
node2 = Node("Lamborgini")
node3 = Node("Porshe")
node4 = Node("Tesla")

#Link All Nodes
linkedList.head.next = node2
node2.next = node3
node3.next = node4
node4 = None

#Print Linked List
linkedList.printList()

#Insert At Front
linkedList.insertAtFront("Bently")
linkedList.insertAtFront("Rivian")

#Print Linked List
linkedList.printList()

#Insert At Back
linkedList.insertAtBack("Nio")
linkedList.insertAtBack("XPEV")


#Print Linked List
linkedList.printList()
