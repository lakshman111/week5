# Read the following code.  Do not run it yet.
#
# What do you think you will see if you run this program?

# If x is not definied in the function, it won't be able to call anything and will have an error

x = 1

def display():
  print(x)
  x = 5

def modify(z):
  z = z + 4

print(x)

# display()
# print(x)

modify(x)
print(x)


