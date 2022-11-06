import heapq
from random import random



class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
        
class MergeKLists:
    def __init__(self) -> None:
        pass

    def merge_k_sorted_lists(self, lists):
        sentinel = ListNode()
        tail_of_merged_list = sentinel

        smallest_remaining_node_per_array = []

        for head in lists:
            if head is not None:
                new_element = (head.val, random(), head)
                heapq.heappush(smallest_remaining_node_per_array, new_element)

        
        while len(smallest_remaining_node_per_array) > 0:
            _value, _rand, smallest_remaining_node = heapq.heappop(smallest_remaining_node_per_array)
            
            tail_of_merged_list.next = smallest_remaining_node
            tail_of_merged_list = tail_of_merged_list.next

            if smallest_remaining_node.next is not None:
                new_element = (smallest_remaining_node.next.val, random(), smallest_remaining_node.next)
                heapq.heappush(smallest_remaining_node_per_array, new_element)

        return sentinel.next
