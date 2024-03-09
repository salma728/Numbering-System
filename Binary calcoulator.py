

# this function represent menu1
def menu1():
    print("**  binary calculator  **")
    print("A)Insert a new number")
    print("B)Exist the programme")


# this function represent menu2
def menu2():
    print("** please select the operation **")
    print("A)Compute one's complement")
    print("B)Compute two's complement")
    print("C)addition")
    print("D)subtraction")


# this function represent the first complement
def first_comp(num):
    first_complement = ''
    for i in num:
        first_complement += '0' if i == '1' else '1'
    return first_complement


"""
# test of function represent the first complement
test = first_comp(str(11101))
print(test)
"""


# this function represent the second complement
def second_complement(num):
    num_str = str(num)
    num_len = len(num_str)
    second_comp = 0
    for i in range(num_len):
        if num_str[i] == '0':
            second_comp += 2 ** (num_len - i - 1)
        else:
            second_comp += 0
    second_comp += 1
    second_complement_str = ""
    while second_comp > 0:
        second_complement_str = str(second_comp % 2) + second_complement_str
        second_comp //= 2
    return second_complement_str


'''
# test of function represent the second complement
test = second_complement(11101)
print(test)
'''


# this function represent the addition
def addition(num_1, num_2):
    i = len(num_1) - 1
    b = len(num_2) - 1
    summon = []
    carry = 0
    while len(num_1) > len(num_2):
        num_2 += "0"
    while len(num_2) > len(num_1):
        num_1 += "0"
    while i >= 0 or b >= 0:
        if num_1[i] == "0" and num_2[b] == "0":
            summon.append(str(carry))
            carry = 0
        elif num_1[i] == "1" and num_2[b] == "1":
            summon.append(str(carry))
            carry = 1
        else:
            if carry == 1:
                summon.append('0')
                carry = 1
            else:
                summon.append('1')
        i -= 1
        b -= 1
    if carry == 1:
        summon.append('1')
    summon.reverse()
    return ''.join(summon)


'''
# test of function represent the addition
test = addition(str(1110), str(11101))
print(test)
'''


# this function represent the subtraction
def subtraction(num_1, num_2):
    first_comp_num2 = first_comp(num_2)
    res = addition(num_1, first_comp_num2)
    final_answer = first_comp(res)
    return final_answer


'''
# test of function represent the subtraction
test = subtraction(str(10001), str(11111))
print(test)
'''
# start of running programme
while True:
    # print start menu1
    menu1()
    # get input from user
    user_choice = input()
    # check if user choice is valid or not
    while user_choice != 'A' and user_choice != 'B':
        # wait until user input a valid choice
        print("please select a valid choice")
        # print menu1 again
        menu1()
        user_choice = input()
    else:
        # in case of valid choice
        if user_choice == "A":
            # get a number user want to convert
            while True:
                num1 = str(input("Enter a binary number: "))
                if not all(i in '01' for i in num1):
                    print("please insert a valid binary number")
                else:
                    break
            # print menu2 and get the operation the user want
            menu2()
            user_oper = input()
            # check if user choice is valid or not
            while user_oper != 'A' and user_oper != 'B' and user_oper != 'C' and user_oper != 'D':
                # wait until user input a valid choice
                print("please select a valid choice")
                menu2()
                user_oper = input()
            else:
                # declare result with an empty value
                result = None
                # check the base user want to convert from and to
                if user_oper == 'A':
                    result = first_comp(num1)
                elif user_oper == 'B':
                    result = second_complement(num1)
                elif user_oper == 'C':
                    while True:
                        num2 = str(input("please insert the second number: "))
                        if not all(i in '01' for i in num2):
                            print("Enter the second binary number again")
                        else:
                            break
                    result = addition(num1, num2)
                elif user_oper == 'D':
                    while True:
                        num2 = input("please insert the second number: ")
                        if not all(i in '01' for i in num2):
                            print("Enter the second binary number again")
                        else:
                            break
                    result = subtraction(num1, num2)
                    # print the result and show it on the screen
                print(result)
        else:
            # Exist program in case user choose B
            break
