from collections import defaultdict, deque

def build_graph_1(ordered_words_list):
    graph = defaultdict(list)
    
    index1, index2 = 0, 1
    
    while index2 < len(ordered_words_list) and index1 < len(ordered_words_list):

        word, next_word = ordered_words_list[index1], ordered_words_list[index2]
        
        i = 0
        while i < len(word) and i < len(next_word) and word[i] == next_word[i]:
            i += 1
            
        if i < len(word) and i < len(next_word):
            index1 = index2
            graph[word[i]].append(next_word[i])
        elif i < len(word): 
            return None
        
        index2 += 1
        
    for word in ordered_words_list:
        for letter in word:
            if letter not in graph:
                graph[letter] = []
                
    return graph

def build_graph_2(ordered_words_list):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    
    for word, next_word in zip(ordered_words_list, ordered_words_list[1:]):
        for letter1, letter2 in zip(word, next_word):
            if letter1 != letter2:
                graph[letter1].append(letter2)
                indegree[letter2] += 1
                break
        else:
            if len(word) > len(next_word): return None, None

    for word in ordered_words_list:
        for letter in word:
            if letter not in graph:
                graph[letter] = []
            if letter not in indegree:
                indegree[letter] = 0
            
    return graph, indegree

def get_alien_dictionary(words):
    graph, indegree = build_graph_2(words)

    if graph is None:
        return ''

    zero_indegree_queue = deque([k for k, c in indegree.items() if c == 0])
    topological_order = []
    while zero_indegree_queue:
        predescessor = zero_indegree_queue.popleft()
        topological_order.append(predescessor)

        for succesor in graph[predescessor]:
            indegree[succesor] -= 1
            if indegree[succesor] == 0:
                zero_indegree_queue.append(succesor)

    return ''.join(topological_order) if len(topological_order) == len(graph) else ''

print(get_alien_dictionary(["za", "z"]))

def alienOrder(words) -> str:
    graph = build_graph_1(words)
    
    if graph is None:
        return ''
    topological_order = []
    
    def traverse_succesors_of(predescessor, visited_set, cycle_set):
        if predescessor in cycle_set:
            return False
        if predescessor in visited_set:
            return True
        visited_set.add(predescessor)
        cycle_set.add(predescessor)
        
        if predescessor in graph:
            for succesor in graph[predescessor]:
                if not traverse_succesors_of(succesor, visited_set, cycle_set):
                    return False
            
        cycle_set.remove(predescessor)
        topological_order.append(predescessor)
        return True
    
    visited_set = set()
    cycle_set = set()
    print(graph)
    for letter in graph:
        if not traverse_succesors_of(letter, visited_set, cycle_set):
            return ''
        
    return "".join(topological_order[::-1])
    