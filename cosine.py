''' waaaavy '''
from math import cos, pi

for i in range(1, 101):
    output = ''
    output += abs(int(cos((i * pi) / 3))) * 'fizz'
    output += abs(int(cos((i * pi) / 5))) * 'buzz'
    output += abs(int(cos(len(output) / 4))) * str(i)
    print(output)
