post = input("Enter the post:")

if " Archit " in post:
    print("The post is talking about Archit.")
else:
    print("The post is not talking about Archit.")
    #Note that the program checks for the exact string " Archit "  with a space before and after,
    #so it will only match posts that contain the exact word " Harry " in that form.
