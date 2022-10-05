import random
  #Sign your name: Tanner Evitts

'''
 1. Make the following program work.
   '''  
print("This program takes three numbers and returns the sum.")
totalNum = 0

for i in range(3):
    x = int(input("Enter a number: "))
    totalNum = totalNum + x
print("The total is:", totalNum)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
even = 2
for e in range(50):
    print(even)
    even  += 2




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
a = 10
while a >= 0:
    print(a)
    a -= 1
print("Blast Off!")
'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

randomizer = random.randrange(10)
print(randomizer)




'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
i = 0
total = 0
while i<7:
    num = int(input("Give me a number, any number: "))
    total += num
    i += 1
print("your total is",total)
