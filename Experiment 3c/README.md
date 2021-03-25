#   Experiment 3c
## Aim of the experiment - Write a program to perform the following operations:
3c)search for a element from B tree


###  procedure for the experiment 
The search operation is the simplest operation on B Tree.
The following algorithm is applied:
Let the key (the value) to be searched by "k".
Start searching from the root and recursively traverse down.
If k is lesser than the root value, search left subtree, if k is greater than the root value, search the right subtree.
If the node has the found k, simply return the node.
If the k is not found in the node, traverse down to the child with a greater key.
If k is not found in the tree, we return NULL.
### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/112514161-09ef2380-8dbb-11eb-80a5-4d50dc428c64.png)



