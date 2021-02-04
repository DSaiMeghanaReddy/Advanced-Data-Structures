#   Experiment 2b
## Aim of the experiment - Write a program for implementing the following sorting methods:
  c)Heap sort

###  procedure for the experiment
In Heap Sort, the given input array is first converted to a Complete Binary Tree. 
Then, a Heapify() function is called that changes the Complete Binary Tree to a Max Heap. 
It is being done so that the largest element from the array can be obtained easily.
Now, once a Max Heap is created, then a swap operation between the Node and the element at the lowest level of the heap is performed. 
After swapping, we get the largest element of the array at the lowest level of the heap, and then a deletion operation is performed. 
In this deletion operation, the node being at the lowest level i.e., the largest element of the array is removed.
The element being removed is inserted in a Queue. 
Since we know that in Heap Sort, we also require a Queue data structure. 
The use of this queue is to hold the removed elements pop then back in the form of a sorted array.
After deletion, the resultant elements will again undergo Heapify() function and all the above mentioned steps will be performed again.


### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/106886434-e5a38e80-6709-11eb-95d7-9b533e407e9d.png)
