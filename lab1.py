import math

S = 0
x = 0.9
i = 1

while math.sin(x)**i/i >= 0.001:
    S = S + math.sin(x)**i/i
    i = i + 1

print(S)