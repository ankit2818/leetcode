# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        q = [(root, 0, 0)]
        while len(q) != 0:
            node, row, col = q.pop()
            if not node:
                continue
            d[(row,  col)].append(node.val)
            d[(row,  col)].sort()
            q.extend([(node.left, row+1, col-1), (node.right, row+1, col+1)])
        
        ans = defaultdict(list)
        k = sorted(list(d.keys()), key = lambda x: (x[1], x[0])) # sort the keys based on col and rows
        for key in k:
            row, col = key
            ans[col].extend(d[key]) # insert values col wise
        return ans.values()
