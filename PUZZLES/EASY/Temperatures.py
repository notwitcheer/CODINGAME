import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

temps = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    temps.append(int(i))

    
if not temps:
    print(0)
    sys.exit()
else:   
    closest = temps [0]
    for t in temps[1:]: 
        if abs(t) < abs(closest) or (abs(t) == abs(closest) and t > closest):
            closest = t



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(closest)