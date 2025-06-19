def factorial(num):
   return 1 if ((num == 1 or num == 0)) else num*factorial(num-1)
num = 5
print("Factorial of given number is :",factorial(num))
