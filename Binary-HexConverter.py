def converte_one (one_value):
    # This loop uses functions built into python to demo decimal/hex/binary representations.
    i = int(one_value)
    print(" Decimal-----", i)
    hex_string = hex((i))
    hex_string_sliced = hex_string[2:]
    print(" Hexadecimal-", hex_string_sliced.upper())
    print(" | 128 | 64  | 32  | 16  |  8  |  4  |  2  |  1  |")
    # this stores the var i as a string
    binary_string = bin(i)
    # formating the string to line up with line 21
    binary_string_sliced =binary_string[2:]
    while len(binary_string_sliced) < 8:
        binary_string_sliced = str(0) +  binary_string_sliced
    print(binary_string_sliced.replace("", "  |  ")[1: -1])
    print()

def converter0_256 ():
    # This loop uses functions built into python to demo decimal/hex/binary representations.
    for i in range (256):
        print(" Decimal-----", i)
        hex_string = hex((i))
        hex_string_sliced = hex_string[2:]
        print(" Hexadecimal-", hex_string_sliced.upper())
        print(" | 128 | 64  | 32  | 16  |  8  |  4  |  2  |  1  |")
        # this stores the var i as a string
        binary_string = bin(i)
        # formating the string to line up with line 21
        binary_string_sliced =binary_string[2:]
        while len(binary_string_sliced) < 8:
            binary_string_sliced =  str(0)+ binary_string_sliced
        print(binary_string_sliced.replace("", "  |  ")[1: -1])
        print()

def binary_hex():
    # User inputs and function calls
    print("This program will demonstrate Integer values 0-256, ")
    print ("reperesented as Binary tables and Hexadecimal  ")
    print ("")
    all_or_one = input("Convert Integer to HEX and Binary Y/N ?")
    Run_all = ""
    if all_or_one == "Y" or all_or_one == "y":
        one_value = input("Convert an integer from 0-256 : ")
        converte_one(one_value)
    else:
        Run_all = input("Show all 0-256 Hex and Binary values  Y/N ?")
    if Run_all == "Y"  or Run_all == "y" :
        converter0_256()

binary_hex()


