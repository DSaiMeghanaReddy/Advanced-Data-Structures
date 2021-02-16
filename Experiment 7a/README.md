#   Experiment 1a
## Aim of the experiment - Write a program to perform the following operations:
7a)Insert an element into a AVL tree



###  procedure for the experiment Insertion of a key 
To make sure that the given tree remains AVL after every insertion, we must augment the standard BST insert operation to perform some re-balancing. 
Following are two basic operations that can be performed to re-balance a BST without violating the BST property (keys(left) < key(root) < keys(right)). 
1) Left Rotation 
2) Right Rotation
Let the newly inserted node be w 
1) Perform standard BST insert for w. 
2) Starting from w, travel up and find the first unbalanced node. Let z be the first unbalanced node, y be the child of z that comes on the path from w to z and w be the grandchild of z that comes on the path from w to z. 
3) Re-balance the tree by performing appropriate rotations on the subtree rooted with z. There can be 4 possible cases that needs to be handled as x, y and z can be arranged in 4 ways. Following are the possible 4 arrangements: 
a) y is left child of z and x is left child of y (Left Left Case) 
b) y is left child of z and x is right child of y (Left Right Case) 
c) y is right child of z and x is right child of y (Right Right Case) 
d) y is right child of z and x is left child of y (Right Left Case)
Following are the operations to be performed in above mentioned 4 cases. In all of the cases, we only need to re-balance the subtree rooted with z and the complete tree becomes balanced as the height of subtree (After appropriate rotations) rooted with z becomes same as it was before insertion.


### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/108041437-89732f80-7064-11eb-9384-400d5b595eb8.png)
