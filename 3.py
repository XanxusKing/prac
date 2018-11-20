finished = False
result = 0
while not finished:
    try:
        result=int(input("enter your marks"))
        finished=true

    except ValueError: # TODO - add something after except
        print("Please enter a valid integer")
print("Valid result is:", result)