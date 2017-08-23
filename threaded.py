''' yes thank you this is my very good code '''
import math
import threading
import time

range_max = 101
class Base(threading.Thread):
    ''' print numbers '''
    def run(self):
        for i in range(1, range_max):
            if i % 3 and i % 5:
                print('\n%d' % i, end='', flush=True)
            else:
                print()
            time.sleep(1)

class Fizz(threading.Thread):
    ''' print Fizz when numbers are divisible by 3 '''
    def run(self):
        for i in range(1, int(math.ceil(range_max/3))):
            time.sleep(2.8)
            print('Fizz', end='', flush=True)
            time.sleep(0.2)

class Buzz(threading.Thread):
    ''' print Buzz when numbers are divisible by 5 '''
    def run(self):
        for i in range(1, int(math.ceil(range_max/5))):
            time.sleep(5)
            print('Buzz', end='', flush=True)

Base().start()
Fizz().start()
Buzz().start()
