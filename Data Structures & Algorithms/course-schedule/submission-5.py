class Solution:
    nodes = None
    nodeVisited = None

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.nodes = dict()
        self.nodeVisited = dict()

        for idx in range(numCourses):
            self.nodes[idx] = set()

        for item in prerequisites:
            self.nodes[item[0]].add(item[1])

        for key in range(numCourses):
            self.nodeVisited[key] = self.traverse(key, set())
            if not self.nodeVisited[key]:
                return False

        return True
                

    def traverse(self, currentKey, currentPath):
        if currentKey in currentPath:
            return False

        if currentKey in self.nodeVisited:
            return self.nodeVisited[currentKey]

        output = True
        for key in self.nodes[currentKey]:
            output = output and self.traverse(key, currentPath.union({currentKey}))

        self.nodeVisited[currentKey] = output
        return output