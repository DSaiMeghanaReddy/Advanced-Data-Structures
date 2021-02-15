#   Experiment 4c
## Aim of the experiment - Write a program to perform the following operations:
4b)Search an element from a Min-Max heap



###  procedure for the experiment  
heap can be used to search whether an element is in it or not with O(logN) time complexity.
You need to search through every element in the heap in order to determine if an element is inside
If you have reached a node with a lower value than the element you are searching for, you don't need to search further from that node. 
However, even with this optimization, search is still O(N) (need to check N/2 nodes in average).
 
### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/107990626-d4585d00-6ffa-11eb-8e1a-e784bab8a6a8.png)
