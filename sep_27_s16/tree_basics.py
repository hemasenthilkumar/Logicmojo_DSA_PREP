"""
Level starts with 0 
Height/Depth starts with 1

Common operations in tree

create, insert, search, delete

Structure

class Node{
  data
  node left
  node right
}

Properties
- for n node, there will be n-1 edges
- depth of any node is length of path from root to that node
- height of a node is the longest path from node to leaf node

 root
  |
  | depth
  |
 node
  |
  | height
  |
 leaf


Tree Traversals

1. Depth First Search
    - Pre-order (DLR)
    - Inorder (LDR)
    - Post-order (LRD)
2. Breadth First Search -> Level order traversing
"""
