
def q1():
  bool1 = True
  bool2 = False
  print(bool1 and bool2)
  print(bool1 or bool2)

def q2():
  num = int(input("Enter an integer: "))
  print(num != 0)

def q3():
  num = float(input("Enter a number: "))
  print(num >= 0 and num <= 10)

def q4():
  food = input("Input food: ")
  drink = input("Input drink: ")
  print(food != "pizza" or drink != "pop")

def q5():
  num = int(input("Enter an integer: "))
  integer = num % 2
  bool = integer == 0
  print(f"The integer {num} is {bool}.")

#Do not edit code after this
#Comment out the followwing code when running tests

# q1()
# q2()
# q3()
# q4()
# q5()
