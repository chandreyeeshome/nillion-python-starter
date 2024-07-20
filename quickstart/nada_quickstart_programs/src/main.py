# PROGRAM TO COMPUTE FACTORIAL OF 10 USING FUNCTION

from nada_dsl import *

def factorial(n):
    # Define party (variables)
    party1 = Party(name="party1")
    result = SecretInteger(Input(name="output", party=party1))
    one = SecretInteger(Input(name="one", party=party1))
    
    # Initialize result to 1
    if n == 0 or n == 1:
        result = one
    else:
        for i in range(1, n):
            result = result * (one + Integer(i))

    return result

def nada_main():
    # Define party (variables)
    party1 = Party(name="party1")

    # Compute the factorial of 10
    output = factorial(10)

    # Return the outputs
    return [Output(output, "output", party1)]

#########################################################################################################

# # PROGRAM TO COMPUTE THE LAST NUMBER OF A FIBONACCI SERIES OF LENGTH 10

# from nada_dsl import *

# def nada_main():

#     # Define party (variables)
#     party1 = Party(name="party1")

#     # Declaring 3 variables
#     a = SecretInteger(Input(name="a", party=party1))
#     b = SecretInteger(Input(name="b", party=party1))

#     # Compute Fibonacci series of length 10
#     for i in range(2,10):
#       c = a + b
#       a = b
#       b = c

#     # Return the outputs
#     return [Output(c, "c", party1)]

#########################################################################################################

# # PROGRAM TO COMPUTE FACTORIAL OF 10

# from nada_dsl import *

# def nada_main():

#     # Define party (variables)
#     party1 = Party(name="party1")

#     # Declaring 3 variables
#     output = SecretInteger(Input(name="output", party=party1))
#     one = SecretInteger(Input(name="one", party=party1))
#     # limit = SecretInteger(Input(name="limit", party=party1))

#     # Compute the factorial of 10
#     for i in range(1,10):
#       output = output*(one + Integer(i))

#     # Return the outputs
#     return [Output(output, "output", party1)]


#########################################################################################################

# # PROGRAM TO COMPUTE (a+b+c)^3 = a^3 + b^3 + c^3 + 3(a+b)(b+c)(c+a)

# from nada_dsl import *

# def nada_main():

#     # Define party (variables)
#     party1 = Party(name="party1")

#     # Declaring 3 variables
#     a = SecretInteger(Input(name="a", party=party1))
#     b = SecretInteger(Input(name="b", party=party1))
#     c = SecretInteger(Input(name="c", party=party1))

#     # Compute the output for (a+b+c)^3
#     # output = a**Integer(3) + b**Integer(3) +c**Integer(3) + Integer(3)*(a+b)*(b+c)*(c+a)
#     output = a*a*a + b*b*b +c*c*c + Integer(3)*(a+b)*(b+c)*(c+a)

#     # Return the outputs
#     return [Output(output, "output", party1)]
