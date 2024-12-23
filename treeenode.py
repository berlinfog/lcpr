from collections import deque
class TreeNode:
    def __init__(self,x:int):
        self.val = x
        self.left = None
        self.right = None

def printTree(root:TreeNode):
    if not root:
        return
    queueTree = deque([root])
    while queueTree:
        node = queueTree.popleft()
        print("val is ",node.val)
        if node.left:
            queueTree.append(node.left)
        if node.right:
            queueTree.append(node.right)

def printPre(root:TreeNode):
    if root == None:
        return
    printPre(root.left)
    print("val is",root.val)
    printPre(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
printPre(root)



class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    # 根节点的路径权重和是 1
    q.append(State(root, 1))

    while q:
        cur = q.popleft()
        # 访问 cur 节点，同时知道它的路径权重和
        print(f"depth = {cur.depth}, val = {cur.node.val}")

        # 把 cur 的左右子节点加入队列
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))





class Solution:
    def __init__(self):
        # 记录最小深度（根节点到最近的叶子节点的距离）
        self.minDepthValue = float('inf')
        # 记录当前遍历到的节点深度
        self.currentDepth = 0

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # 从根节点开始 DFS 遍历
        self.traverse(root)
        return self.minDepthValue

    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return

        # 前序位置进入节点时增加当前深度
        self.currentDepth += 1

        # 如果当前节点是叶子节点，更新最小深度
        if root.left is None and root.right is None:
            self.minDepthValue = min(self.minDepthValue, self.currentDepth)

        self.traverse(root.left)
        self.traverse(root.right)

        # 后序位置离开节点时减少当前深度
        self.currentDepth -= 1

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        q = deque([root])
        # root 本身就是一层，depth 初始化为 1
        depth = 1

        while q:
            sz = len(q)
            # 遍历当前层的节点
            for _ in range(sz):
                cur = q.popleft()
                # 判断是否到达叶子结点
                if cur.left is None and cur.right is None:
                    return depth
                # 将下一层节点加入队列
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            # 这里增加步数
            depth += 1
        return depth
    