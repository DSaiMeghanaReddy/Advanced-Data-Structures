#   Experiment 3
## Aim of the experiment - Write a program to perform the following operations:
7a)Insertion and deletion of element in B tree



###  procedure for the experiment 
Insertion of element in B tree
If the tree is empty, allocate a root node and insert the key.
Update the allowed number of keys in the node.
Search the appropriate node for insertion.
If the node is full, follow the steps below.
Insert the elements in increasing order.
Now, there are elements greater than its limit. So, split at the median.
Push the median key upwards and make the left keys as a left child and the right keys as a right child.
If the node is not full, follow the steps below.
Insert the node in increasing order.
deletion of element in B tree
Before going through the steps below, one must know these facts about a B tree of degree m.
A node can have a maximum of m children. 
A node can contain a maximum of m - 1 keys. 
A node should have a minimum of ⌈m/2⌉ children. 
A node (except root node) should contain a minimum of ⌈m/2⌉ - 1 keys.
There are three main cases for deletion operation in a B tree.
Case I
The key to be deleted lies in the leaf. There are two cases for it.
1.The deletion of the key does not violate the property of the minimum number of keys a node should hold.
2.The deletion of the key violates the property of the minimum number of keys a node should hold. In this case, we borrow a key from its immediate neighboring sibling node in the order of left to right.
First, visit the immediate left sibling. If the left sibling node has more than a minimum number of keys, then borrow a key from this node.
Else, check to borrow from the immediate right sibling node.
If both the immediate sibling nodes already have a minimum number of keys, then merge the node with either the left sibling node or the right sibling node. This merging is done through the parent node.
Case II
If the key to be deleted lies in the internal node, the following cases occur.
1.The internal node, which is deleted, is replaced by an inorder predecessor if the left child has more than the minimum number of keys.
2.The internal node, which is deleted, is replaced by an inorder successor if the right child has more than the minimum number of keys.
3.If either child has exactly a minimum number of keys then, merge the left and the right children.
 After merging if the parent node has less than the minimum number of keys then, look for the siblings as in Case I.
 Case III
 In this case, the height of the tree shrinks. If the target key lies in an internal node, and the deletion of the key leads to a fewer number of keys in the node (i.e. less than the minimum required), then look for the inorder predecessor and the inorder successor. If both the children contain a minimum number of keys then, borrowing cannot take place. This leads to Case II(3) i.e. merging the children.
Again, look for the sibling to borrow a key. But, if the sibling also has only a minimum number of keys then, merge the node with the sibling along with the parent. Arrange the children accordingly (increasing order).





### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/112364755-dd74d200-8cfc-11eb-9119-73080a023906.png)

