Two approaches for tractable (non-exponential) algorithms are:
1. Identifying a greedy algorithm
2. Using dynamic programming

### Dynamic Programming
Two different techniques we can use to implement a dynamic programming solution:

#### Memoization
Where we add caching to a function (that has no side effects). In DP, it is typically used on recursive functions for a top-down solution that starts with the initial problem and then recursively calls itself to solve smaller problems

#### Tabulation
Tabulation uses a table to keep track of subproblem results and works in a bottom-up manner; solving the smallest subproblems before the large ones, in an iterative manner. The words 'tabulation' and 'dp' are used interchangeably.


### Dyanmic Process
1. Start with the recursive backtracking solution
2. Optimize by using a memoization table (top-down DP)
3. Remove the need for recursion (bottom-up DP)
4. Apply final tricks to reduce the time/memory complexity


## Steps to solve a DP problem
[Article here](https://www.freecodecamp.org/news/follow-these-steps-to-solve-any-dynamic-programming-interview-problem-cc98e508cd0e/)

### 1. How to recognize a DP problem
- DP is essentially just an optimization technique
- DP is a method for solving problems by breaking them down into a collection of simpler subproblems (solve once and store)
- **Need to ask self whether your problem solution can be expressed as a function of solutions to similar smaller problems**

### 2. Identify problem variables
- Typically you will have one or two changing parameters, but could be any number
- Eg. Fibonacci (one changing), Compute edit distance between strings (two changing)
- A way to determine number of changing params is to list examples of several subproblems and compare the parameters

### 3. Clearly express the currence relation
- Ask: How do problems relate to each other? Helps with getting to how do you compute the main problem?

Spike Example:
> More formally, if our speed is S, position P, we could go from (S,P) to:
> 1. (S, P+S)  # if we do not change the speed
> 2. (S-1, P+S-1)  # if we change the speed -1
> 3. (S+1, P+S+1)  # if we change the speed +1
> If we can find a way to stop in any of the subproblems above, then we can also stop from (S,P). This is because we can transition from (S,P) to any of the three options

> canStop(S,P) = canStop(S, P+S) or canStop(S-1, P+S-1) or canStop(S+1, P+S+1)

### 4. Identify the base cases
- A base case is a subproblem that doesn't depend on any other subproblem. Identify at which point problem cannot continue being simplified
- One reason could be that one of the parameters would be become a value that is not possible given the constraints of the problem

> In the example, we have two changing parameters S and P. When might these not be legal?
> 1. P should be within the bounds of the given runway
> 2. P cannot be such that runway[P] is false because that would mean that we're standing on a spike
> 3. S cannot be negative and S==0 indicates we're done

- It can be difficult converting assertions we make about parameters into programmable base cases. This is because in addition to listing the assertions if you want to make your code look concise and not check for unnecessary conditions, you also need to think about which of these conditions are even possible.

> 1. P < 0 or P >= len(runway) seems like the right thing to do. An alternative to consider would be making P == end of runway a base case.
> 2. Could check if runway[P] is false
> 3. Could check S < 0 and S == 0. However, here we can reason that it is impossible for S to be < 0 because S decreases by at most 1, so it would have to go through S == 0 case beforehand. Therefore S == 0 is a sufficient base case for the S parameter

### 5. Decide if you want to implement it iteratively or recursively
|   | Recursive  | Iterative  |
|:-:|---|---|
| Asymptotic Time Complexity  | Same assuming memo  | Same  |
| Memory Usage  | Recursive stack, sparse memo  | Full memo  |
| Execution Speed  | Often faster depending on the input | Slower, needs to do same work regardless of the input |
| Stack Overflow | Problem  | Not an issue as long as enough memory for memo  |
| More intuitive/Easier to Implement | Often easier to reason about  | Most people find it hard to reason through  |

### 6. Add memoization
- Used for storing the results of expensive function calls (cache results)
- Usually treating memoization as a function result cache is the most intuitive way to implement it
1. Store your function result into your memory before every return statement
2. Look up the memory for the function result before you start doing any other computation

### 7. Determine time complexity
- Some steps for computing complexity:
1. Count the number of states - this will depend on the number of changing parameters in your problem
2. Think about the work done per each state. In other words, if everything else but one state has been compute, how much work do you have to do to compute that last state?

> In the example problem, the number of states is |P|*|S| where 
> - P is the set of all positions (|P| indicates the number of elements in P)
> - S is the set of all speeds
> The work doen per each state is O(1) in this problem because, given all other states, we simply have to look at 3 subproblems to determine the resulting state
> As we noted in the code before, |S| is limited by length of the runway (|P|), so we could say that the number of states is |P|**2 and because work done per each state is O(1), then the total time complexity is O(|P|^2)