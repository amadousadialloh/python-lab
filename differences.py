# Exercise 1

def getNane():
    name = input('What is your name')
    return name


getNane()

# Exercise 2
def reverseIt():
    string = 'a man, a plan, a canal, frenemises!'
    reverse = ''
    for i in range(len(string)):  
        reverse = string[len(string) - (i + 1)] + reverse  
    print(reverse)

reverseIt()

# Exercise 3
def swapEm ():
    a = 10
    b = 30
    temp = 0
    temp = b
    b = a
    a = temp
    print(f'a is now {a} and b is now {b}' )
    
swapEm()    


# Exercise 4
def multiply (arr):
    if len(arr) == 0:
        return 1  
    
    total = 1 
    for num in arr: 
        total *= num  
  


result = multiply([2, 2, 2])  
print(result) 
 
#  Exercise 5
def fizzbuzzer (x):
    if (x%(3*8)) == 0:
        return 'fizzbuzz'
    elif (x%3) == 0:
        return 'fizz'
    elif ( x%5 == 0 ):
        return 'buzz'
    else: return 'archer'
    
    


# Exercie 6        
def nthFibonacciNumber():
    fibs = [1, 1]
    num = input('Which Fibonacci number do you want? ') 

   
    while len(fibs) < int(num):  
        length = len(fibs)
        nextFib = fibs[length - 2] + fibs[length - 1]  
        fibs.append(nextFib)  
    
    print(f'The {num}th Fibonacci number is {fibs[int(num) - 1]}')

nthFibonacciNumber()
        