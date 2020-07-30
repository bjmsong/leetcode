# 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。 
# 
#  设计一个算法来序列化和反序列化二叉搜索树。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化
# 为最初的二叉搜索树。 
# 
#  编码的字符串应尽可能紧凑。 
# 
#  注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to string
        bfs
        """
        if not root:
            return
        result = []
        from collections import deque
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        return result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree
        索引为k的节点，子节点为2k+1,2k+2
        """
        if not data:
            return
        root = TreeNode(data[0])
        from collections import deque
        q = deque()
        q.append([root, 0])
        while q:
            for _ in range(len(q)):
                node, k = q.popleft()
                if 2 * k + 2 > len(data):
                    return root
                node1 = TreeNode(data[2 * k + 1])
                node.left = node1
                node2 = TreeNode(data[2 * k + 2])
                node.right = node2
                q.append([node1, 2 * k + 1])
                q.append([node2, 2 * k + 2])

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    s = Codec()
    print(s.serialize(root))
    node = s.deserialize(s.serialize(root))
    print(node)
