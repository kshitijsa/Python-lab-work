n = int(input("enter the number of rows"))
x = n
sp = " "
while (x > 0):
  y = 2 * (n - x)
  print("*" * x + y * sp + "*" * x)
  x = x - 1
