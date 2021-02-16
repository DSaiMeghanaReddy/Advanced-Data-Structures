#   Experiment 7b
## Aim of the experiment - Write a program to perform the following operations:
7b)Delete an element from AVL tree


###  procedure for the experiment 
The following implementation uses the recursive BST delete as basis. 
In the recursive BST delete, after deletion, we get pointers to all ancestors one by one in bottom up manner. 
So we don’t need parent pointer to travel up. The recursive code itself travels up and visits all the ancestors of the deleted node.
1) Perform the normal BST deletion.
2) The current node must be one of the ancestors of the deleted node. Update the height of the current node.
3) Get the balance factor (left subtree height – right subtree height) of the current node.
4) If balance factor is greater than 1, then the current node is unbalanced and we are either in Left Left case or Left Right case. To check whether it is Left Left case or Left Right case, get the balance factor of left subtree. If balance factor of the left subtree is greater than or equal to 0, then it is Left Left case, else Left Right case.
5) If balance factor is less than -1, then the current node is unbalanced and we are either in Right Right case or Right Left case. To check whether it is Right Right case or Right Left case, get the balance factor of right subtree. If the balance factor of the right subtree is smaller than or equal to 0, then it is Right Right case, else Right Left case.



### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/108045547-98a8ac00-7069-11eb-8599-fd04fd73231a.png)
