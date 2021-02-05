#   Experiment 1b
## Aim of the experiment - Write a program to perform the following operations:
1b)Delete an element from Binary search tree


###  procedure for the experiment Delete an element from Binary search tree

When we delete a node, three possibilities arise. 
1) Node to be deleted is leaf: Simply remove from the tree. 
2) Node to be deleted has only one child: Copy the child to the node and delete the child 
3) Node to be deleted has two children: 
Find inorder successor of the node. 
Copy contents of the inorder successor to the node and delete the inorder successor. 
Note that inorder predecessor can also be used. 
The important thing to note is, inorder successor is needed only when right child is not empty. In this particular case, inorder successor can be obtained by finding the minimum value in right child of the node.


 


### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/107022951-fcaab500-67cb-11eb-860c-e47a0c644a93.png)


