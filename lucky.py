''' sometimes you have to make your own luck '''
from random import choice, seed

seed(4910128406)  # py 3.2+
pattern = [choice(['', 'fizz', 'buzz', 'fizzbuzz']) for n in range(15)] * 7

for n in range(100):
    print(pattern[n] or n+1)
