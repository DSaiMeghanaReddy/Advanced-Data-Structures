#   Experiment 8a
## Aim of the experiment - Write a program to perform the following operations:
8a)Insert an element into a Red-Black tree.



###  procedure for the experiment 
While inserting a new node, the new node is always inserted as a RED node. After insertion of a new node, if the tree is violating the properties of the red-black tree then, we do the following operations.
Recolor
Rotation
Let x be the newly inserted node.
Perform standard BST insertion and make the colour of newly inserted nodes as RED.
If x is the root, change the colour of x as BLACK (Black height of complete tree increases by 1).
Do the following if the color of x’s parent is not BLACK and x is not the root. 
a) If x’s uncle is RED (Grandparent must have been black from property 4) 
(i) Change the colour of parent and uncle as BLACK. 
(ii) Colour of a grandparent as RED. 
(iii) Change x = x’s grandparent, repeat steps 2 and 3 for new x. 
b) If x’s uncle is BLACK, then there can be four configurations for x, x’s parent (p) and x’s grandparent (g) (This is similar to AVL Tree) 
(i) Left Left Case (p is left child of g and x is left child of p) 
(ii) Left Right Case (p is left child of g and x is the right child of p) 
(iii) Right Right Case (Mirror of case i) 
(iv) Right Left Case (Mirror of case ii)



### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/114156008-bdb9ec80-993f-11eb-8eb6-a0b699ed47db.png)
