# TC: O(M*N), SC: O(M*N)
def longestCommonSubsequence(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

# TC: O(M*N), SC: O(min(M, N))
def longestCommonSubsequence_opt(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(2)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i % 2][j] = 1 + dp[(i - 1)%2][j - 1]
                continue
            dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

    return dp[len(text1) % 2][-1]

a = '583wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcacehchzvfrkmlnozjkpqpxrjxkitzyxacbhhkicqcoendtomfgdwdwfcgpxiqvkuytdlcgdewhtaciohordtqkvwcsgspqoqmsboaguwnnyqxnzlgdgwpbtrwblnsadeuguumoqcdrubetokyxhoachwdvmxxrdryxlmndqtukwagmlejuukwcibxubumenmeyatdrmydiajxloghiqfmzhlvihjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztq'
b = a[::-1]
print(len(a) - longestCommonSubsequence_opt(a, b))