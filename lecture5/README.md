---
title: "Python Programming - Lecture 5"
---

### Object Oriented Programming (OOP)

```

import random

class Animal(object):
    def __init__(self):
        self.color = None
        self.position = {x:0, y:0}

    def move(self, x, y):
        self.x = x
        self.y = y
        print('move to x: {}, y: {}'.format(x, y))

class Giraff(Animal):
    def __init__(self, name):
        self.name = name

    def left_foot_forward(self):
        print('left_foot_forward')

    def right_foot_forward(self):
        print('right_foot_forward')

    def left_foot_backward(self):
        print('left_foot_backward')

    def right_foot_backward(self):
        print('right_foot_backward')

class CrazyGiraff(Giraff):
    def __init__(self):
        self.facebook_followers = []

    def dance(self):        
        steps = random.randint(3, 8)
        for _ in range(steps):
            move = random.randint(1, 4)
            if move == 1:
                self.left_foot_forward()
            elif move == 2:
                self.left_foot_backward()
            elif move == 3:
                self.right_foot_forward()
            elif move == 4:
                self.right_foot_backward()

    def backflip(self):
        print('Awesome backflip')

    def split(self):
        print('Crazy split')


```

* * *

### Chapter 9 - Python’s Built-in Functions
IDLE

##### input()
```
>>> year = input('Year of birth: ')
Year of birth: 2000
>>> 'You were born in {}'.format(year)
'You were born in 2000'
>>>
```

##### len(), min(), max(), sum()
```
>>> A = [5, 4, 10, 20, 30]
>>> len(A)
5
>>> min(A)
4
>>> max(A)
30
>>> sum(A)
69
```

##### type conversion
```
>>> a = '5.5'
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: '5.5'
>>> float(a)
5.5
>>> bool(a)
True
>>> a = 0
>>> bool(a)
False
>>> a = 10
>>> a = '10'
>>> a + 20
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a + 20
TypeError: must be str, not int
>>> int(a) + 20
30
```

##### abs()
```
abs(-10)
>>> if abs(steps) > 0:
	print('character is moving')
-> Recover (by typing on a line)
```

##### dir(), help()
```
>>> dir('hello')
>>> help('hello'.upper)
>>> 'hello'.upper()
'HELLO'
```

##### eval()
```
eval()
>>> formula = input('Enter formula: ')
Enter formula: 12*52
>>> eval(formula)
624
```

##### File open / write

```
>>> file = open('C:\Users\jason\Documents\hello.txt')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> file = open('C:\\Users\\jason\\Documents\\hello.txt')
>>> print(file.read())
fdsfasfsfasfas
>>>
KeyboardInterrupt
>>> file = open('C:\\hello.txt')

>>> file = open('C:\\Users\\jason\\Documents\\hello2.txt', 'w')
>>> file.write('This is a test.')
15
>>> file.close()
```

##### Quiz
```
>>>bool(4)
>>>a, b = 10, ‘20’
>>>a+b
```

* * *

### Chapter 10 - Useful Python Modules

##### turtle
```
>>> import turtle
```

##### random
```
>>> import random
>>> A = [10, 20, 30, 40, 50]
>>> random.choice(A)
50
>>> random.choice(A)
30
>>> random.choice(A)
50
>>> random.choice(A)
30
>>> random.choice(A)
40
```

##### time
```
>>> import time
>>> time.time()
1511711769.7801137
>>> time.time()
1511711773.4365573
>>> time.asctime()
'Sun Nov 26 07:56:51 2017'
>>> time.localtime()
time.struct_time(tm_year=2017, tm_mon=11, tm_mday=26, tm_hour=7, tm_min=57, tm_sec=12, tm_wday=6, tm_yday=330, tm_isdst=0)
>>> time.localtime()[0]
2017
>>>
```

##### pickle
```
>>> A = [10, 20, 30, 40, 50]
>>> import pickle
>>> pickle.dump(A, open('my_data.p', 'wb'))

# Close IDLE and re-launch IDLE
>>> A = pickle.load(open('my_data.p','rb'))
>>> A
[10, 20, 30, 40, 50]
```

* * *

### Lubuntu virtual machine
Make sure everybody got the Lubuntu copy and have a working version

### Code Combat
