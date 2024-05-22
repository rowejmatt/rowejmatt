# Create a function that will find numbers that evenly divide down to 90-110
# Create ranges within those numbers
# Find numbers outside these ranges that need to separately split

import sys


### Take an input of first weight and desired riffle weight

original_Num = 200
count = 0
good_num = []

# Division has finished when condition is met
for x in range(original_Num, 10000, 10):
    
    division = 0
    
    divide_Num = x
    
    count += 1
    
    while divide_Num > 550:
        
        division += 1
        
        result = divide_Num / 2
        
        if result >= 450 and result <= 550:
            good_num.append(x)
            break
        
        divide_Num = result

print(good_num)
# Start with first number, next number printed is when the increment is more than 10
## Range of numbers where the split is first, second, third or fourth

flag = True

for current, next_num in zip(good_num, good_num[1:]):
    if flag:
        print(current)
        flag = False

    if next_num - current > 10:
        print(f'{current}, {next_num}')
        
        
def awk_num(a: int, b:int):
    """a is starting weight, b is desired weight"""
    
    c = b*1.1
    d = b - (b*.1)
    riffle = 0
    
    while a > c:
                
        riffle += 1
           
        a = a / 2
        
        accumalation = a + a/2 # Check whether accumation is within ranges
        
        print('a is more than c')
        
    print(f'a is {a}')

    return print(riffle)
    
awk_num(a=2267, b=500)


sys.exit()

# Go through numbers between ranges to find if the divisions are between 90 and 100 and at which split.
# Each first in range is 220 repeated difference
# Each second in range is 360 repeated difference
First_riffle = 10
Second_riffle = 5

# Riffle to < 90, keeping track of riffles, keep lowest amount so add from bottom
# Riffle to known range then keep left pan
# Create graphs to how to come to conclusions

if fourth_riffle == True:
    
    fourth_riffle + third_riffle
    
    # This wants to be 10% of desired end weight
    
    if result > 85 and result < 110:
    # Print out that you need to keep fourth riffle and third riffle.
        print(result)