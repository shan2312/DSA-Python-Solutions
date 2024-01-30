from collections import deque

# TC: O(N^3 + M*K), SC: O(N + m*k)
def is_word_breakable_bfs(word, dictionary):
    q = deque([0])
    visit = set([0])
    dictionary_set = set(dictionary)

    while q:
        current_node = q.popleft()
        if current_node == len(word):
            return True

        for end in range(current_node + 1, len(word) + 1):
            if end in visit:
                continue
            if word[current_node: end] in dictionary_set:
                q.append(end)
                visit.add(end)

    return False

def is_word_breakable_dfs2(word, dictionary):
    def dfs_helper(start_index):
        if start_index >= len(word):
            return True


        for w in dictionary:
            if word[start_index:(start_index + len(w))] == w and dfs_helper(start_index + len(w)):
                return True

        return False

    return dfs_helper(0)
            


# TC: O(N^2*K)
def is_word_breakable_dfs(word, dictionary):
    dp = {}
    dictionary_set = set(dictionary)
    def dfs_helper(start_index):
        if start_index >= len(word):
            return True

        if start_index in dp:
            return dp[start_index]

        for end_index in range(start_index + 1, len(word) + 1):
            if word[start_index:end_index] not in dictionary_set:
                continue
            if dfs_helper(end_index):
                dp[start_index] = True
                return dp[start_index]
        dp[start_index] = False
        return dp[start_index]

    return dfs_helper(0)

def is_word_breakable_dp(word, dictionary):
    dp = [False] * (len(word) + 1)
    dp[-1] = True

    for i in range(len(dp) - 2, -1, -1):
        for w in dictionary:
            w_len = len(w)
            if word[i: (i + w_len)] != w:
                continue
            dp[i] |= dp[i + w_len]
    return dp[0]




print(is_word_breakable_dfs2('cars', ['car', 'ca', 'rs']))
