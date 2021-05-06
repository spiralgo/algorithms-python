class Solution:

        def depthSum(self, nestedList, currLevel=1) -> int:
            """
            :type nestedList: List[NestedInteger]
            :rtype: int
            """
            ret = 0
            for element in nestedList:
                if element.isInteger():
                    ret += currLevel * element.getInteger()
                else:
                    ret += self.depthSum(element.getList(), currLevel=currLevel + 1)
            return ret


if __name__ == "__main__":
    print("Currently not testable.")

