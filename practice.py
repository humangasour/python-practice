def main():
    # n = int(input('Enter the number: '))
    # fibbonacci(n)

    # n1 = int(input('Enter first number: '))
    # n2 = int(input('Enter second number: '))
    # gcd(n1, n2)

    s = input('Enter a string: ')
    pallindrome(s)

####### NUMBER FUNCTIONS #######

def sum_of_n(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print(sum)

def sum_of_odd_n(n):
    sum = 0
    for i in range(1, (2 * n) + 1, 2):  # (2 * n) because we're taking the step as 2
        sum = sum + i
    print(sum)

def factorial(n):
    fact = 1  #initliaze with 1 and not 0
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

def lcm(n1, n2):
    if n1 > n2: 
        greater = n1
    else: 
        greater = n2
    while True:  #loop will keep on running until we break out of it explicitly
        if (greater % n1 == 0) and (greater % n2 == 0):  #if the number is perfectly divisible by both n1 and n2
            print(f"lcm is {greater}")  #formatted string
            break  # using break to get out of the loop
        else:
            greater += 1 

def gcd(n1, n2):
    if n1 < n2:
        smaller = n1
    else: 
        smaller = n2
    gcd = 1  # setting gcd as 1 initially
    for i in range(2, smaller + 1): # starting the loop from 2 because 1 can devide any number so no point 
        if (n1 % i == 0) and (n2 % i == 0):
            gcd = i     # this will keep over riding the value of gcd whenever the condition is true so in the end we will have the highest common factor
    print(gcd)

def sum_of_digits(n):
    sum = 0
    temp = n  #storing the number in temp so that we can change the value of n and the original number remains intact
    while temp > 0:  
        digit = temp % 10    #EXTRACTING the digit using modulas operator
        sum   = sum + digit  #ADDING the digit to sum 
        temp  = temp // 10   #REDUCING the temp so we can extract the next digit
    print(sum)

def armstrong(n): # the sum of digits (raised to the power n) of a number is equal to the number itself. Where n is the length of digits
    sum = 0
    temp = n    #storing the number in temp so that we can change the value of n and the original number remains intact
    length = len(str(n)) # we use the len function to find the length of the str(n). str is used because len function only accepts a string parameter
    while temp > 0:
        digit = temp % 10               #EXTRACTING the digit using modulas operator
        sum   = sum + digit ** length   #ADDING the digit(raised to power length) to sum 
        temp  = temp // 10              #REDUCING the temp so we can extract the next digit
    if n == sum:     #compare n(original number) with sum and NOT temp with sum
        print(f"{n} is an armstrong number")
    else:
        print(f"{n} is not an armstrong number")

def fibbonacci(n):  # 0 1 1 2 3 5 8
    n1 = 0
    n2 = 1
    if n <= 0:
        print("Enter a positive integer")
    elif n == 1:
        print(n1)
    else:
        for i in range(1, n+1):
            print(n1, end=", ") # first time it will print 0 and then it will keep printing the updated value of n1
            sum = n1 + n2  
            n1 = n2 
            n2 = sum
        print()    

####### STRING FUNCTIONS #######  

def reverse(s):
    rev = ""
    for i in s:     # to get the value of every character in string 
        rev = i + rev        
    print(rev)

def pallindrome(s):
    rev = ""
    for i in s:
        rev = i + rev
    if rev == s:
        print(f"{s} is pallindrome")
    else:
        print(f"{s} is not a pallindrome")
        
####### PATTERNS #######

def star_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("*", end="")
        print()

def reverse_star_triangle(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(end=" ")

        for j in range(1, i+1):
            print("*", end="")
        print()

def star_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(end=" ")
        
        for j in range(1, i+1):
            print("*", end="")
        
        for j in range(2, i+1):
            print("*", end="")
        print()

def number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
        print()

def reverse_number_triangle(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(end=" ")
        for j in range(i, 0, -1):
            print(j, end="")
        print()

def number_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, (n-i)+1):
            print(end=" ")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i+1):
            print(j, end="")
        print()


if __name__ == "__main__":
    main()