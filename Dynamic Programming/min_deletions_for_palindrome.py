

def is_palindrome(s):
    l, r = 0, len(s) - 1
    
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            
        else:
            return False
            
    return True

#Brute force 2^n
def minDeletions(self, Str, n):
    s_list = list(Str)

    def get_deletions_from(start, end):
        if start >= end or is_palindrome(Str[start: (end + 1)]):
            return 0
    
        if s_list[start] == s_list[end]:
                return get_deletions_from(start +1, end - 1)
            
        else:
            return 1 + min(get_deletions_from(start + 1, end), get_deletions_from(start, end - 1))
            
    return get_deletions_from(0, n - 1)
    

def get_min_deletions(s):
    s1 = s
    s2 = s[::-1]

    dp = [[0] * (len(s2) + 1) for _ in range(2)]

    for i in range(1, len(dp[0])):
        for j in range(1, len(dp[0])):
            dp[i%2][j] = (1 + dp[(i - 1)%2][j - 1]) if s1[i - 1] == s2[j - 1] else max(dp[(i - 1)%2][j], dp[i%2][j - 1])

    return (len(s) - dp[len(s) %2][-1])

print(get_min_deletions('583wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoqhnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcacehchzvfrkmlnozjkpqpxrjxkitzyxacbhhkicqcoendtomfgdwdwfcgpxiqvkuytdlcgdewhtaciohordtqkvwcsgspqoqmsboaguwnnyqxnzlgdgwpbtrwblnsadeuguumoqcdrubetokyxhoachwdvmxxrdryxlmndqtukwagmlejuukwcibxubumenmeyatdrmydiajxloghiqfmzhlvihjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztq'))