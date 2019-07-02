# Job Dependencies


## Summary

Take a representation of jobs and their dependencies and produce an order
in which to carry out the jobs successfully (i.e. all jobs are executed 
only after the jobs it depends on have been completed).


## Input & Output

A string representation of a list of jobs with corresponding dependencies.
 > Input: `"a => , b => c, c => "`

The above means that Job `c` must happen before Job `b` and Job `a` can 
happen at any time.

 > Output: `"cab"` or `"cba"`


## Design

- Parse input string and create a directed graph from input
- For a "correct" ordering to exist, the graph must also be acyclic
- Perform a topological sort on the graph, if such an order doesn't exist,
then the graph is cyclic and by definition of the problem we cannot have 
cyclic dependencies.
- Print the topological sort
