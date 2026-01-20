def third(a):
    print(int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out


def second(a, b):
    c = a + b
    print(c)  # --> The output is called 'Stack Trace'

    # Calling the third function
    third(c)


def first():
    # Calling the second function
    second("The output is called ", "'Stack Trace'")

first()
