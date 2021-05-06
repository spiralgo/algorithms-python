class Solution:
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        depth = self.findDepth(nestedList)
        return self.sumDepth(nestedList, depth)

    def findDepth(self, nestedList):
        if len(nestedList) == 0:
            return 0
        depth = list()
        for ni in nestedList:
            if not ni.isInteger():
                depth.append(self.findDepth(ni.getList()))
        return max(depth) + 1 if len(depth) > 0 else 1

    def sumDepth(self, nestedList, depth):
        s = 0
        for ni in nestedList:
            if ni.isInteger():
                s += ni.getInteger() * depth
            else:
                s += self.sumDepth(ni.getList(), depth - 1)
        return s