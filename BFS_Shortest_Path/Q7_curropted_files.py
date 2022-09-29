"""
The file directory system on your computer has been corrupted by a virus. Random files have been copied throughout, 
and files are have been moved to new locations. You need your team's new engineer to go through and find certain files, 
but they don't want to do it because they're worried that they might have to go very deep into the file directory system 
to find files.
You need to convince them that they will NOT need to go that deep. To do so, you'll compute the deepest that they will need to go.
You'll be given a list of required files, a hash map that maps directory names to a list of elements that are in that directory 
(these will either be directories themselves or filenames), and lastly you'll be given a string representing the directory 
that you start in.
You must return the minimum depth that your new engineer must go through to find all of the required files. 
You can assume that this is structured like a normal file system (it's impossible that inside of directory A you have directory B, 
but inside of directory B you have directory A).
"""
from collections import deque

CANNOT_FIND_ALL_FILES = -1

def get_min_depth_to_find_all_files(directory_structure, required_files, root_directory):

    queue = deque()
    root_tuple = (root_directory, 0)
    queue.append(root_tuple)

    visited = set()
    visited.add(root_directory)

    while queue:
        present_node, distance_so_far = queue.popleft()

        if present_node in required_files:
            required_files.remove(present_node)

        if len(required_files) == 0:
            return distance_so_far

        if '.' in present_node:
            continue

        for neighbor in directory_structure[present_node]:

            if neighbor in visited: continue
            
            neighbor_tuple = (neighbor, distance_so_far + 1)
            queue.append(neighbor_tuple)
            visited.add(neighbor)

    return CANNOT_FIND_ALL_FILES






directory_structure = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E", "F"],
    "D": ["1.js", "2.js"],
    "E": ["G", "H"],
    "F": ["I", "J"],
    "G": ["3.js", "4.js"],
    "H": ["K"],
    "I": ["L", "M"],
    "J": ["emptyFile.js"],
    "K": ["5.js"],
    "L": ["6.js", "7.js", "8.js"],
    "M": ["N"],
    "N": ["9.js", "O"],
    "O": ["P", "Q"],
    "Q": ["R", "S"],
    "R": ["randomFile.js"],
    "S": ["otherRandomFile.js"]
}
required_files = ["1.js", "2.js", "3.js", "4.js", "5.js", "6.js", "7.js", "8.js", "9.js"]
root_directory = "A"

print(f"Your answer: {get_min_depth_to_find_all_files(directory_structure, required_files, root_directory)}")
print(f"Correct answer: {6}")
print()