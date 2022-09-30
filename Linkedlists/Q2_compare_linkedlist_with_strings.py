
# Given two linked lists L1 and L2 in which in every node a string is stored. The task is to check whether the strings combining all the nodes are similar or not. 


# Input: L1 = [“He”, “llo”, “wor”, “ld”], 
#            L2 = [“H”, “e”, “ll”, “owo”, “r”, “ld”]
# Output: true
# Explanation: both lists makes the string of “Helloworld”.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def compare_string_linkedlists(list1, list2):
    start_index1 = start_index2 = 0

    while list1 or list2:
        if list1 and list1.val == '':
            list1 = list1.next

        if list2 and list2.val == '':
            list2 = list2.next

        s1 = list1.val[start_index1] if list1 and list1.val != '' else ''
        s2 = list2.val[start_index2] if list2 and list2.val != '' else ''


        if s1 != s2:
            return False
            
        else:
            if start_index1 < len(list1.val) - 1:
                start_index1 += 1
            else:
                start_index1 = 0
                list1 = list1.next if list1 else list1

            if start_index2 < len(list2.val) - 1:
                start_index2 += 1
            else:
                start_index2 = 0
                list2 = list2.next if list2 else list2

    return True


if __name__ == '__main__':
    l1 = Node('s')
    l1.next = Node('@')
    l1.next.next = Node('')
    l1.next.next.next = Node('ch')

    l2 = Node('s@')
    l2.next = Node('ch')
    l2.next.next = Node('')
    # l2.next.next.next = Node('')
    print(compare_string_linkedlists(l1, l2))




    