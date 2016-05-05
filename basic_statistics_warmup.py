###############################################################################
# Basic Statistics Warmup
###############################################################################
# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

N = int(raw_input())
x = map(int, raw_input().rstrip().split(' '))

# Mean
x_mean = float(sum(x)) / N

# Median
x.sort()
if N % 2 == 0:
    x_median = float((x[N/2 - 1] + x[N/2])) / 2
else:
    x_median = x[N/2]

# Mode
count_occur = [x.count(i) for i in x]
x_mode = x[count_occur.index(max(count_occur))]

# Standard Deviation
x_std_dev = (sum([(i - x_mean) ** 2 for i in x]) / N-1) ** 0.5

# Lower and Upper Boundary of the 95% Confidence Interval for the mean
x_low_conf_interv = x_mean - 1.96 * (x_std_dev / N ** 0.5) 
x_hi_conf_interv = x_mean + 1.96 * (x_std_dev / N ** 0.5)

print round(x_mean, 1)
print round(x_median, 1)
print x_mode
print round(x_std_dev, 1)
print x_low_conf_interv, x_hi_conf_interv
