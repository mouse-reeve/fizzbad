''' waaaavy '''
import math

for i in range(1, 101):
    output = ''
    output += abs(int(math.cos((i * math.pi) / 3))) * 'fizz'
    output += abs(int(math.cos((i * math.pi) / 5))) * 'buzz'
    output += abs(int(math.cos(len(output) / 4))) * str(i)
    print(output)
