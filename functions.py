def greet():
    """
    Simple function that just print hello
    :return: None
    """
    print("Hello!")

def greet2(name):
    """
    Simple function that greets a person
    :param name: Name of the person
    :return: None
    """
    print(f"Hello, {name}")

greet2("Andre")

def special_op(a=1,b=1): #a=1 and b=1 is defining the implicit values (1,1)
    '''
    Special op is 10*a+b
    :param a: first number
    :param b: second number
    :return: value, 10*a+b
    '''
    return 10*a+b

print(special_op(10,2))
print(special_op(2,10))
result = special_op(8,9)
print(f"the special op for 8 and 9 is: {result}")
print(special_op(b=8, a=9))
print(special_op()) #runs with the implicit values
print(special_op(a=9))

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name}, {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name("John", "Doe"))
bond_greet(bondise_name())