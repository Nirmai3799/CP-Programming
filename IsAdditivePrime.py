# IsAdditivePrime: Additive primes can be defined as prime numbers where the sum of its digits is a prime number. Write a function isAdditivePrime that takes n as an integer and returns True if n is an Additive Prime and False otherwise.
# Some of the Additive Primes are 2, 3, 5, 7, 11, 23, 29, and etc.
# 29 = 2 + 9 = 11 = 1 + 1 = 2 and 2 is a prime number.
# Here are sample test cases:
# assert (isAdditivePrime(2) == True)
# assert (isAdditivePrime(3) == True)
# assert (isAdditivePrime(5) == True)
# assert (isAdditivePrime(13) == False)
# assert (isAdditivePrime(23) == True)
# assert (isAdditivePrime(29) == True)
# assert (isAdditivePrime(41) == True)
# assert (isAdditivePrime(98) == False)
# assert (isAdditivePrime(198) == False)
# assert (isAdditivePrime(290) == False)
# assert (isAdditivePrime(67) == True)
# assert (isAdditivePrime(97) == False)
# print("All test cases passed... :-)")
def fun_nth_additive_prime(n):
   if(n == 0):
       return 2
   elif(n == 1):
       return 3
   x = 1
   y = 4
   while(x<=n):
       if(additivePrime(y)):
           x = x+1
       if(x == n):
           return y
       y = y+1
 
def additivePrime(n):
   if(isPrime(n) and isPrime(sumDigit(n))):
       return True
 
def sumDigit(n):
   sum = 0
   while(n!=0):
       sum = sum + n%10
       n = n//10
   return sum
 
def isPrime(n):
   if (n < 2):
       return False
   if (n == 2):
       return True
   if (n % 2 == 0):
       return False
   maxFactor = round(n**0.5)
   for factor in range(3,maxFactor+1,2):
       if (n % factor == 0):
           return False
   return True

