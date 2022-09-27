

"""
Facebook often shows a section called “People You May Know” on a user's feed to recommend them to add new friends on Facebook. Imagine that we want to write an algorithm that outputs friend recommendations for a given user.
We'll write a simple algorithm: anyone who is a “friend of a friend” should be a friend recommendation (unless, of course, this individual is already friends with our given user). For example, if Alice is friends with Bob and Bob is friends with Carla (but Alice is not friends with Carla), then Alice should see Carla in her “People You May Know” section.
Each of our users will be represented by an ID (a number) in the range [0, n - 1] where n is the total number of users. You'll receive two pieces of information as input: a userId (this represents the user for whom we would like to provide friend recommendations) and an adjacency matrix. In our adjacency matrix, if matrix[r][c] = 1, then user r is friends with user c (and vice versa). Otherwise, matrix[r][c] should be 0. You should return a list of user IDs that are valid individuals for our given user's “People You May Know” section. This list can be in any order.
"""
from collections import deque

def get_neighbors(user_id, friendships):
    user_friendships = friendships[user_id]

    for neighbor_id, is_friend in enumerate(user_friendships):
        if neighbor_id == user_id:
            continue
        if is_friend == 0:
            continue
        yield neighbor_id

def get_friend_recommendations(user_id, friendships):
    friend_recommendations = []

    queue = deque()
    user_tuple = (user_id, 0)
    queue.append(user_tuple)

    visited = set()
    visited.add(user_id)

    while queue:
        node, distance_so_far = queue.popleft()

        if distance_so_far == 2:
            friend_recommendations.append(node)

        if distance_so_far > 2:
            continue
        
        neighbors = get_neighbors(node, friendships)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            neighbor_tuple = (neighbor, distance_so_far + 1)
            queue.append(neighbor_tuple)
            visited.add(neighbor)

    return friend_recommendations

    



user_id = 0
friendships = [
    [1,1,0,0,1,1],
    [1,1,1,0,0,1],
    [0,1,1,1,0,0],
    [0,0,1,1,0,1],
    [1,0,0,0,1,0],
    [1,1,0,1,0,1],
]

print(f"Your answer: {get_friend_recommendations(user_id, friendships)}")
print(f"Correct answer: {[2,3]}")
print()