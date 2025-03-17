# My first python project in PLP
# Building a mini calculator
print("This is a mini calculator that calculate only two value of your choice... ")
firstNumber = float(input("Enter your first number: "))
secondNumber = float(input("Enter your second number: "))
arithmetic = input ("Enter arithmetic operator(+, /, *): ")
if arithmetic == "+":
  print(firstNumber + secondNumber)
elif arithmetic == "-":
  print(firstNumber - secondNumber)
elif arithmetic == "*":
  print(firstNumber * secondNumber)
elif arithmetic == "/":
  print(firstNumber / secondNumber)
elif arithmetic == "//":
  print(firstNumber // secondNumber)
elif arithmetic == "%":
  print(firstNumber % secondNumber)
else:
  print("Try again")
  
#Now the mini calculator is set and ready to test......
#You must check it out 
