# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12

def change_x():
    global x #makes it so we can reference the defined global x, as opposed to a local x variable
    x = 99

change_x()

# This prints 12. What do we have to modify in change_x() to get it to print 99?
print(x)


# This nested function has a similar problem.

def outer():
    y = 120

    def inner():
        nonlocal y #Since the inner() function is within the outer(), it will have access to any defined variables  in outer()
        #but using nonlocal allows us to use the newly defined variable as opposed to the previous
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print(y)


outer()
