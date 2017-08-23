''' waaaavy '''
import math

for i in range(1, 101):
    if abs(math.sin((i * math.pi)/3) * math.sin((i * math.pi)/5)) > 10 ** -10:
        print('%d' % i)
    elif abs(math.sin((i * math.pi)/3) * math.sin((i * math.pi)/5)) < 10 ** -20:
        print('FizzBuzz')
    elif abs(math.sin((i * math.pi)/3)) < 10 ** -10:
        print('Fizz')
    else:
        print('Buzz')
