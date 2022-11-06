class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        res = []

        for portion in path_list:
            if portion == "." or portion == "":
                continue
            elif res and portion == "..":
                res.pop()
            elif portion != "..":
                res.append(portion)

        cannonical_path = "/" + "/".join(res)
        return cannonical_path
