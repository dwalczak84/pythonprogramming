p = int(raw_input())
q = int(raw_input())
output = []
   
for i in range(p, q + 1):
    num_digits = 0
    temp = i
    
    while temp != 0:
        num_digits  += 1
        temp /= 10
    temp = i * i
    l = temp / (10 ** num_digits)
    r = temp - l * (10 ** num_digits)
    
    if (r + l == i):
        output.append(i)
    
if len(output) == 0:
    print 'INVALID RANGE'
else:
    for i in output:
        print i,
        
