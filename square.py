a=int(input("Enter number:"))
'''in this give int before input because if you dont give it the input function returns a string, not a number.
 So, when you try to square the input, it performs string concatenation.In this code, we use the int function to convert 
 the input string to an integer before storing it in the a variable. This way, 
 when we perform the multiplication, it will be a mathematical multiplication of two numbers instead of string concatenation.'''
print("sqaure is",a*a)
