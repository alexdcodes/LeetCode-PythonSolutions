class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def iterative(root):
            q=deque()
            visited=set()
            if root:
                q.append(root)
            while q:
                src=q[-1]
                if src in visited:
                    q.pop()
                    l.append(src.val)
                else:
                    visited.add(src)
                    if src.right:
                        q.append(src.right)
                    if src.left:
                        q.append(src.left)
        iterative(root)
        return l
