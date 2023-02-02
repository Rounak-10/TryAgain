class Computer(): # This class always vacant, Class ke andar jo "Variables/Attributes" and "Methods/Functions"
                  # hote hai, unko call karna hota hai. Sirf Object banake Class ko Call karne se kuch nahi hoga.
    def config(a):
        print("I have a laptop")

obj1 = Computer() # This is only for Object creation, not for "calling Class".
obj1.config() # Now we are actually calling Function/Method of "Computer Class". Jo bhi declare kiya hoga
              # "function definition" ke time, wahi print hoga.

Computer.config(a=obj1) # Ye 2nd tarika hai, class and uske andar jo methods/variable hai  unko call karne ka.

a = 5 # This "a" is object of Integer Class.
b = "a" # Similarly, "a" is object of String Class.

a.bit_length() # If we see "bit_length" function(Ctrl+Click), then we see that it is having "self" one positional argument,
                # but we are not passing it in here. coz we are instatiating object "a" with this function. So "self"
                # is taking "a" as a parameter.
print(len(b))
