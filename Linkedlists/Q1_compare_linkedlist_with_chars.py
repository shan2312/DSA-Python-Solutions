
# Given two strings, represented as linked lists (every character is a node in a linked list). Write a function compare() that works similar to strcmp(), i.e., it returns 0 if both strings are the same, 1 if the first linked list is lexicographically greater, and -1 if the second string is lexicographically greater.

# a -> b -> c
# a -> b -> c 
# return 0


# Input: list1 = g->e->e->k->s->a
#           list2 = g->e->e->k->s->b
# Output: -1
# Explanation: “geeksb” is lexicographically greater than “geeksa”.

# Input: list1 = g->e->e->k->s->a
#           list2 = g->e->e->k->s
# Output: 1
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def compare_char_linkedlists(list1, list2):
    
    while list1 and list2:
        if list1.val > list2.val:
            return 1
            
        elif list1.val < list2.val:
            return -1
        
        list1 = list1.next
        list2 = list2.next

    return 1 if list1 else -1 if list2 else 0



if __name__ == '__main__':
    l1 = Node('s')
    l1.next = Node('a')
    l1.next.next = Node('c')
    l1.next.next.next = Node('h')

    l2 = Node('s')
    l2.next = Node('a')
    l2.next.next = Node('c')
    l2.next.next.next = Node('h')

    print(compare_char_linkedlists(l1, l2))