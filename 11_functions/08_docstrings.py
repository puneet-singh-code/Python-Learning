# def sum(a,b):
#      """This will sum two numbers"""
#      c = a + b
#      return c
# print(sum.__doc__)

x =10 # Global variable
def modify_global():
    global x
    x =5 # Modifies the global x
modify_global()
print(x) # Output: 5
