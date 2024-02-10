# coder1918
1. from queue import PriorityQueue
2. Median of 2 sorted arrays - Recursive binary search
3. Reverse KGroup - iterate and reverse up until K, make K as the head and recursively repeat the process
4. Use stack for trapped water - current, popped, top element => (min(current, top) - popped) gives the height of trapped water
5. Use Hash map to increment the character count and maintain formed counter if the frequency of a character matches.
6. Generic string stategy - hot => h*t, *ot, h*t(generic strings) - create adj graph and find path from src string to dest string
7. Rotated sorted with duplicates - if mid_val > right_val: left = mid + 1; if mid_val == right_val: right -= 1; if mid_val < right_val: right -= 1
8. Use deque to maintain k elements in monotonic increasing sequence, add indices of elements into the queue and to find the lenght of the window/queue (current index - first index in the queue)
9. Preorder list contains root as the first element - to construct a tree we pop first element and create a tree node and repeat this process
10. Factors of a number - range(2, sqrt(num) + 1)
11. DP - top-down (big to small); bottom-up(small to big problem)
12. predict the winner - alternatively choose turns like -> nums[left] - findWinner(left+1, right) => player1 - player2 + player1 - player2...
13. use stack for merge intervals - compare each interval with top interval in the stack. => curr_start <= prev_end(from interval in the stack)
14. Counting sort and quick select(random pivot, split the array based on pivot, repeat the process by checking if k <= len(left) or if k > len(left) + len(mid)) 
15. 3 sum - Compliment approach, sort and 2 pointer approach, split array into -ves, +ves, 0's
16. In Kadane's algorithm - use if conditions instead of max() function
17. Rotate array - using reverse() function(in-place), using an additional space by iteratively replacing current index position with (index+k)%n position
18. Random pick with weight - prefix sum(cummulative sum) with binary search - data sampling
19. Duplicates - Negative marking, cyclic sort, binary search(count of each num), sort and check adjacent elements, fast and slow pointers
20. Updating and maintaining a sequence or a heap or an array with specific elements in it(like in LIS) or of specific length
21. Longest String chain - sort, dfs, split word by excluding each character in it, track visited, words_set for constant look up time
22. House Robber - recurrence relation - dp[i] = max(dp[i-1], dp[i-2]+nums[i])
23. K-closest elements - binary search for closest element to the target and use sliding window to find k closest elemnts
24. Surrounded regions - go into the grid through borders and mark each visited cell as 'Y' and finally fill back 'Y' -> '0' and '0' -> 'X'
25. Earliest when they become friends - Sort in chronological order, once all the friends are connected number of components becomes 1

26. Be quick/fast; Be Clear; Be Mindfull; Stay Focused; Act smart; stay excited; stay relaxed; TALK SLOW; THINK BEFORE I TALK; Maintain clarity; 
27. Hand gestures to communicate confidently; Dont repeat after myself; Cut straight to the point
28. Steps
    1. Remember to ask for clarification of the problem first - 
        1. Can I code in Python?
        2. if given array/list sorted or not; range/size of the input; if builtin functions can be used;
    2. Use Large inputs as test cases while working on logic; Use small while executing;
    3. Write down algorithm(steps in English); Write down Hints if any; Write down key points in the problem statement
    4. Ask interviewer if I can start coding; 
    5. If anything went wrong stay calm and try to resolve it if possible otherwise move on; Dont let the situation disturb meeee
    6. While writing down the algorithm, Mention time complexities - Best and worst(most cases)
    7. Think of worst cases - around the problem

IMP points

whats the problem is?

What do I have?

What should be the result?

test cases

Approach