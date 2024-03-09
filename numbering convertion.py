# Salma Mohamed Abdalhaliem Ali

# this function represent menu1
def menu1():
    print("** numbering system convert **")
    print("A)Insert a new number")
    print("B)Exist a program")


# this function represent menu2
def menu2():
    print("**please select the base you want to convert a number from**")
    print("A)Decimal")
    print("B)Binary")
    print("C)Octal")
    print("D)hexadecimal")


# this function represent menu3
def menu3():
    print("**please select the base you want to convert a number to**")
    print("A)Decimal")
    print("B)Binary")
    print("C)Octal")
    print("D)hexadecimal")


# this function convert from decimal to decimal
def decimal_to_decimal(num):
    return num


'''
test = decimal_to_decimal(5)
print(test)
'''


# this function convert from decimal to binary
def decimal_to_binary(num):
    num = int(num)
    if num == 0:
        return num
    else:
        binary_num = ""
        while num > 0:
            remainder = num % 2
            binary_num = str(remainder) + binary_num
            num //= 2
    return binary_num


'''
# test of convert from decimal to binary
test = decimal_to_binary(5)
print(test)
'''


# this function convert from decimal to octal
def decimal_to_octal(num):
    num = int(num)
    if num == 0:
        return num
    else:
        octal_num = ""
        while num > 0:
            remainder = num % 8
            octal_num = str(remainder) + octal_num
            num //= 8
    return octal_num


"""
# test of convert from decimal to octal 
test = decimal_to_octal(5)
print(test)
"""


# this function convert from decimal to hexadecimal
def decimal_to_hexadecimal(num):
    num = int(num)
    if num == 0:
        return num
    else:
        hexa_num = ""
        while num > 0:
            remainder = num % 16
            if remainder == 10:
                remainder = "A"
            elif remainder == 11:
                remainder = "B"
            elif remainder == 12:
                remainder = "C"
            elif remainder == 13:
                remainder = "D"
            elif remainder == 14:
                remainder = "E"
            elif remainder == 15:
                remainder = "F"
            hexa_num = str(remainder) + hexa_num
            num //= 16
    return hexa_num


"""
# test of convert from decimal to hexadecimal 
test = decimal_to_hexadecimal(5)
print(test)
"""


# this function convert from binary to decimal
def binary_to_decimal(num):
    binary_num = num[::-1]
    decimal_num = 0
    for i in range(len(binary_num)):
        decimal_num += (int(binary_num[i]) * (2 ** i))
    return decimal_num


'''
# test of convert from binary to decimal 
test = binary_to_decimal(str(11101))
print(test)
'''


# this function convert from binary to binary
def binary_to_binary(num):
    return num


'''
# test of convert from binary to binary 
test = binary_to_binary(11101)
print(test)
'''


# this function convert from binary to octal
def binary_to_octal(num):
    decimal = binary_to_decimal(num)
    octal_num = decimal_to_octal(decimal)
    return octal_num


'''
# test of convert from binary to octal
test = binary_to_octal(str(11101))
print(test)
'''


# this function convert from binary to hexadecimal
def binary_to_hexadecimal(num):
    decimal = binary_to_decimal(num)
    hexa_num = decimal_to_hexadecimal(decimal)
    return hexa_num


'''
# test of convert from binary to hexadecimal 
test = binary_to_hexadecimal(str(11101))
print(test)
'''


# this function convert from octal to decimal
def octal_to_decimal(num):
    octal_num = num[::-1]
    decimal_num = 0
    for i in range(len(octal_num)):
        decimal_num += (int(octal_num[i])) * (8 ** i)
    return decimal_num


'''
# test of convert from octal to decimal 
test = octal_to_decimal(str(77))
print(test)
'''


# this function convert from octal to binary
def octal_to_binary(num):
    decimal = octal_to_decimal(num)
    binary_num = decimal_to_binary(decimal)
    return binary_num


'''
# test of convert from octal to binary
test = octal_to_binary(str(77))
print(test)
'''


# this function convert from octal to octal
def octal_to_octal(num):
    return num


'''
# test of convert from octal to octal
test = octal_to_octal(str(77))
print(test)
'''


# this function convert from octal to hexadecimal
def octal_to_hexadecimal(num):
    decimal_num = octal_to_decimal(num)
    hexadecimal_num = decimal_to_hexadecimal(decimal_num)
    return hexadecimal_num


"""
# test of convert from octal to hexadecimal
test = octal_to_hexadecimal(str(77))
print(test)
"""


# this function convert from hexadecimal to decimal
def hexadecimal_to_decimal(num):
    hexa_num = num[::-1]
    decimal_num = 0
    for i in range(len(hexa_num)):
        if hexa_num[i] == 'A':
            decimal_num += 10 * (16 ** i)
        elif hexa_num[i] == 'B':
            decimal_num += 11 * (16 ** i)
        elif hexa_num[i] == 'C':
            decimal_num += 12 * (16 ** i)
        elif hexa_num[i] == 'D':
            decimal_num += 13 * (16 ** i)
        elif hexa_num[i] == 'E':
            decimal_num += 14 * (16 ** i)
        elif hexa_num[i] == 'F':
            decimal_num += 15 * (16 ** i)
        else:
            decimal_num += (int(hexa_num[i])) * (16 ** i)
    return decimal_num


"""
# test of convert from hexadecimal to decimal
test = hexadecimal_to_decimal(str(4F))
print(test)
"""


# this function convert from hexadecimal to binary
def hexadecimal_to_binary(num):
    decimal_num = hexadecimal_to_decimal(num)
    binary_num = decimal_to_binary(decimal_num)
    return binary_num


"""
# test of convert from hexadecimal to binary
test = hexadecimal_to_binary(str(4F))
print(test)
"""


# this function convert from hexadecimal to octal
def hexadecimal_to_octal(num):
    decimal_num = hexadecimal_to_decimal(num)
    octal_num = decimal_to_octal(decimal_num)
    return octal_num


"""
# test of convert from hexadecimal to octal
test = hexadecimal_to_octal(str(4F))
print(test)
"""


# this function convert from hexadecimal to hexadecimal
def hexadecimal_to_hexadecimal(num):
    return num


"""
# test of convert from hexadecimal to hexadecimal
test = hexadecimal_to_hexadecimal(str(4F))
print(test)
"""

# start of running program
while True:
    # print start menu1
    menu1()
    # get input from user
    user_choice = str(input())
    # check if user choice is valid or not
    while user_choice != 'A' and user_choice != 'B':
        # wait until user input a valid choice
        print("please select a valid choice")
        # print menu1 again
        menu1()
        user_choice = str(input())
    else:
        # in case of valid choice
        if user_choice == "A":
            # get a number user want to convert
            print("please insert a number")
            # convert number to upper case
            number = str(input().upper())
            # print menu2 and get the base user want to convert from
            menu2()
            base_from = str(input())
            # check if user choice is valid or not
            while base_from != 'A' and base_from != 'B' and base_from != 'C' and base_from != 'D':
                # wait until user input a valid choice
                print("please select a valid choice")
                menu2()
                base_from = str(input())
            else:
                # print menu3 and get the base user want to convert to
                menu3()
                base_to = str(input())
                # check if user choice is valid or not
                while base_to != 'A' and base_to != 'B' and base_to != 'C' and base_to != 'D':
                    # wait until user input a valid choice
                    print("please select a valid choice")
                    menu3()
                    base_to = str(input())
                else:
                    # declare result with an empty value
                    result = None
                    # check the base user want to convert from and to
                    if base_from == 'A':
                        if base_to == 'A':
                            result = decimal_to_decimal(number)
                        elif base_to == 'B':
                            result = decimal_to_binary(number)
                        elif base_to == 'C':
                            result = decimal_to_octal(number)
                        elif base_to == 'D':
                            result = decimal_to_hexadecimal(number)
                    elif base_from == 'B':
                        if base_to == 'A':
                            result = binary_to_decimal(number)
                        elif base_to == 'B':
                            result = binary_to_binary(number)
                        elif base_to == 'C':
                            result = binary_to_octal(number)
                        elif base_to == 'D':
                            result = binary_to_hexadecimal(number)
                    elif base_from == 'C':
                        if base_to == 'A':
                            result = octal_to_decimal(number)
                        elif base_to == 'B':
                            result = octal_to_binary(number)
                        elif base_to == 'C':
                            result = octal_to_octal(number)
                        elif base_to == 'D':
                            result = octal_to_hexadecimal(number)
                    elif base_from == 'D':
                        if base_to == 'A':
                            result = hexadecimal_to_decimal(number)
                        elif base_to == 'B':
                            result = hexadecimal_to_binary(number)
                        elif base_to == 'C':
                            result = hexadecimal_to_octal(number)
                        elif base_to == 'D':
                            result = hexadecimal_to_hexadecimal(number)
                # print the result and show it on the screen
                print(result)
        else:
            # Exist program in case user choose B
            break
