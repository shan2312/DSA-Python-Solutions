from collections import defaultdict, deque

def build_graph(edges, n):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for node1, node2 in edges:
        graph[node2].append(node1)
        indegree[node1] += 1

    for node in range(n):
        if node not in graph:
            graph[node] = []
        if node not in indegree:
            indegree[node] = 0

    return graph, indegree

def get_course_schedule(prerequisites, numCourses):
    graph, indegree = build_graph(prerequisites, numCourses)

    zero_indegree_queue = deque([k for k in range(numCourses) if indegree[k] == 0])
    topological_order = []

    while zero_indegree_queue:
        predescessor_course = zero_indegree_queue.popleft()
        topological_order.append(predescessor_course)

        for successor_course in graph[predescessor_course]:
            indegree[successor_course] -= 1

            if indegree[successor_course] == 0:
                zero_indegree_queue.append(successor_course)

    return topological_order if len(topological_order) == numCourses else []


def get_course_schedule_dfs(prerequisites, numCourses):
    graph, indegree = build_graph(prerequisites, numCourses)
    topological_order = []

    def traverse_succesors_of(start_course, visited_set, cycle_set):
        if start_course in cycle_set:
            return False
        if start_course in visited_set:
            return True
        
        visited_set.add(start_course)
        cycle_set.add(start_course)
        
        for succesor_course in graph[start_course]:
            if not traverse_succesors_of(succesor_course, visited_set, cycle_set):
                return False
            
        cycle_set.remove(start_course)
        topological_order.append(start_course)
        return True
    
    visited_set = set()
    cycle_set = set()

    for course in range(numCourses):
        if not traverse_succesors_of(course, visited_set, cycle_set):
            return []
        
    return topological_order[::-1] if len(topological_order) == numCourses else []




print(get_course_schedule_dfs([[1,0],[2,0],[3,1],[3,2]], 4))
print(get_course_schedule_dfs([[1,0]], 2))
print(get_course_schedule_dfs([], 1))