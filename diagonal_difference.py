# Diagonal Difference
# by vatsalchanana
# Given a square matrix of size N×NN×N, calculate the absolute difference 
# between the sums of its diagonals.
# Input Format
# The first line contains a single integer, NN. The next NN lines denote the 
# matrix's rows, with each line containing NN space-separated integers 
# describing the columns.
# Output Format
# Print the absolute difference between the two sums of the matrix's 
# diagonals as a single integer.

# Sample Input
# 
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
# 
# 15
# Explanation
# 
# The primary diagonal is: 
# 11
#       5
#             -12
# 
# Sum across the primary diagonal: 11 + 5 - 12 = 4
# 
# The secondary diagonal is:
#             4
#       5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19 
# Difference: |4 - 19| = 15

#!/bin/python

import sys

def diagonal_difference(n, a):
    c = []
    # Making one dimensional list
    for j in range(n):
        for i in range(n):
            c.append(a[i][j])

    print abs(int(sum(c[0::n+1])) - int(sum(c[n-1:-n+1:n-1])))

    
n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

diagonal_difference(n, a)
