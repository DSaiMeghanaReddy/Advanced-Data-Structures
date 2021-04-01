#   Experiment 12
## Aim of the experiment -  Write a program for implementing  Boyer pattern matching algorithm



###  procedure for the experiment  
Boyer Moore is a combination of following two approaches.
1) Bad Character Heuristic
2) Good Suffix Heuristic
Both of the above heuristics can also be used independently to search a pattern in a text. 
If we take a look at the Naive algorithm, it slides the pattern over the text one by one. 
KMP algorithm does preprocessing over the pattern so that the pattern can be shifted by more than one. 
The Boyer Moore algorithm does preprocessing for the same reason. 
It processes the pattern and creates different arrays for both heuristics. 
At every step, it slides the pattern by the max of the slides suggested by the two heuristics. 
So it uses best of the two heuristics at every step.
Unlike the previous pattern searching algorithms, Boyer Moore algorithm starts matching from the last character of the pattern.
The idea of bad character heuristic is simple. The character of the text which doesn’t match with the current character of the pattern is called the Bad Character. Upon mismatch, we shift the pattern until –
1) The mismatch becomes a match
2) Pattern P move past the mismatched character.
Case 1 – Mismatch become match
We will lookup the position of last occurrence of mismatching character in pattern and if mismatching character exist in pattern then we’ll shift the pattern such that it get aligned to the mismatching character in text T.
Case 2 – Pattern move past the mismatch character
We’ll lookup the position of last occurrence of mismatching character in pattern and if character does not exist we will shift pattern past the mismatching character.



### Output Obtained
![image](https://user-images.githubusercontent.com/77834002/113288653-e113e480-930c-11eb-8e82-0127b125fcab.png)
