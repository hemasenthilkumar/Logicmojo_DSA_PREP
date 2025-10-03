

from collections import deque
from bfs import level_order

class TreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data 
        self.left = left 
        self.right = right 

def remove_node(root, data):
    if not root or root.data == data:
        return None

    queue = deque()
    queue.append(root)

    while queue:
        curr = queue.popleft()
        if curr.data == data:
            curr = None 
            return root 

        if curr.left:
            if curr.left.data == data:
                curr.left = None 
                return root 
            queue.append(curr.left)
        if curr.right:
            if curr.right.data == data:
                curr.right = None 
                return root 
            queue.append(curr.right)
    return root

def delete(root, data):
    # swap the to be deleted node with the bottom right most node
    # delete the bottom right most node 

    queue = deque()
    queue.append(root)
    to_delete = None
    while queue:
        curr = queue.popleft()
        if curr.data == data:
            to_delete = curr
            # keep the loop running to get the last right node
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    print(to_delete, to_delete.data)
    print(curr, curr.data)
    if not to_delete:
        return root
    elif to_delete != curr:
        temp = curr.data
        curr.data = to_delete.data
        to_delete.data = temp
    print("After swapping:")
    print(to_delete, to_delete.data)
    print(curr, curr.data)    
    
    return remove_node(root, data)

if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    root.left = node1 
    root.right = node2 
    node3 = TreeNode(31)
    node4 = TreeNode(61)
    node5 = TreeNode(51)
    node1.left = node3 
    node2.left = node4 
    node2.right = node5
    print("before deleting")
    print(level_order(root))
    for i in [31, 2]:
        root = delete(root, i)
    print("after deleting")
    print(level_order(root))