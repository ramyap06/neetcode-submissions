class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {}

        for r in prerequisites:
            if r[0] not in courses:
                courses[r[0]] = []
            courses[r[0]].append(r[1])

        visiting = set()
        
        def dfs(c):
            if c in visiting:
                # cycle detected
                return False
            if c not in courses or courses[c] == []:
                return True

            visiting.add(c)
            for pre in courses[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            courses[c] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True