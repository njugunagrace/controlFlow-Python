# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numbers():
    x=0
    while x<50:
        x+=1
        if x%2!=0:
            continue
        print(f"{x} is an even number")
     
 #Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.

def prime_numbers(num):
    if num < 2:
        print(f"{num} Not prime")
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} Not prime")
    print(f"{num} is Prime")


#Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(*nums):
    sum=0
    for num in nums:
        if num%2==0:
            sum+=num
        print(sum)
        
        
#Write a function that takes any two integers as input, and prints the sum of all the numbers between 
#the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_3(a, b):
    if a > b:
        a, b = b, a
    total = 0
    for num in range(a, b+1):
        if num % 3 == 0:
            total += num
    print(total)


        
                 
           
            
        
