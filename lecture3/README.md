# Python Programming - Week 3

* * *

### Answers to Last Week's Homework
#### Chapter 3
##### #1: Favorites
```
games = ['baseball', 'football']
foods = ['yogurt', 'steak']
favorites = games + foods
print(favorites)
```

##### #2: Counting Combatants
```
res = (3*25)+(2*40)
print(res)

```

#### #3: Greetings!
```
first_name, last_name = 'John', 'Doe'
str_template = 'Hi there, %s %s!'
print(str_template % (first_name, last_name))

```
* * *

#### Chapter 6
##### #1: The Hello Loop
It will print 'hello 0.'

##### #2: Event Numbers
```
age = int(input("Enter your age: "))
start = 2 if age % 2 == 0 else 1
for x in range(start, age + 1, 2):
    print(x)
```

#### #3: My Five Favorite Ingredients
```
ingredients = ['snails', 'leeches', 'gorilla belly-button lint',
               'caterpillar eyebrows', 'centipede toes']
for i, item in enumerate(ingredients):
    print('%s %s' % (i + 1, item))
```

#### #4: Your Weight on the Moon
```
start = int(input("Enter your weight in kilogram: "))
for w in range(start, start + 16):
    print(w * 0.165)
```

* * *

#### FizzBuzz
```
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
```

* * *

#### Data compression
```
input_str = input('Enter string:')
prev, res, length = '', '', 0


def build_result(s, n, output):
    if n > 1:
        return output + s + str(n)
    else:
        return output + s


for cur in input_str:
    if prev == cur:
        length += 1
    else:
        if length > 0:
            res = build_result(prev, length, res)
        length = 1
    prev = cur
res = build_result(prev, length, res)
print(res)
```
* * *

#### Two Sum - Using bruit force
```
A = [5, 3, 7, 8, 1]
k = 11

res = None
for i in range(len(A)):
    for j in range(i+1, len(A) - i):
        if A[i] + A[j] == k:
            res = [A[i], A[j]]
            break
    if res:
        break
print(res if res else "Not found")
```

#### Two Sum - Using dictionary
```
A = [5, 3, 7, 8, 1]
k = 11

dict = {}
for num in A:
    if num in dict:
        print(k - num, num)
    else:
        dict[k - num] = num
```

#### Two Sum - Using sorting
```
A = [5, 3, 7, 8, 1]
k = 11

A = sorted(A)
i, j = 0, len(A) - 1
while i < j:
    sum = A[i] + A[j]
    if sum < k:
        i += 1
    elif sum > k:
        j -= 1
    else:
        print(A[i], A[j])
        break
```

* * *
* * *
<a name="practice"></a>
### Practices

#### Chapter 7
* Type all examples in chapter #7  (Recycling Your Code With Functions And Modules)

* * *

#### Calculator - Create a calculator that accepts three inputs (a, b and op) where a and b are integers, and op is a string with one of following values: +, -, \*, / or q. If op is 'q', quit program. Use the template below as a skeleton code:

```

def add(a, b):
    pass

def minus(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def calculate(a, b, op):
    pass

if __name__ == "__main__":
    op = ''
    while op != 'q':
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        op = input('Enter +,-,*,/ or q (q for quit)')
        res = calculate(a, b, op)
        print('{} {} {} is {}'.format(a, op, b, res))

```


#### CodeCombat!!!
Play for 20 minutes

* * *
