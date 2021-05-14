import math

class Solution:
    current_best = -1

    def closestValue(self, root, target):
        if root == None:
            return self.current_best
        current_val = root.val
        if self.current_best == -1:
            self.current_best = root.val
        self.current_best = current_val if abs(
            current_val-target) < abs(self.current_best-target) else self.current_best
        if target < current_val:
            self.closestValue(root.left, target)
        elif target > current_val:
            self.closestValue(root.right, target)

        return self.current_best


if __name__ == "__main__":
    pass
