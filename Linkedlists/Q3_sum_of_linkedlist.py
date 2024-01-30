class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    carry = 0
    dummy = curr = LinkedList(0)
    
    while linkedListOne or linkedListTwo or carry != 0:
        digit1 = linkedListOne.value if linkedListOne else 0
        digit2 = linkedListTwo.value if linkedListTwo else 0

        addition = (digit1 + digit2 + carry)
        add_digit = addition % 10
        carry = addition // 10

        new_node = LinkedList(add_digit)
        curr.next = new_node

        curr = curr.next
        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    return dummy.next


if __name__ == '__main__':
    node1 = LinkedList(2)
    node1.next = LinkedList(8)
    node1.next.next = LinkedList(4)
    node1.next.next.next = LinkedList(9)

    node2 = LinkedList(9)
    node2.next = LinkedList(9)
    node2.next.next = LinkedList(9)
    
    sum = sumOfLinkedLists(node1, node2)

    while sum:
        print(sum.value)
        sum = sum.next
