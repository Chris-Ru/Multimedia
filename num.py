import numpy as np

while True:
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Modulus\n12. Tan\n13. Sin\n14. Cos\n15. Exit")
    num = input()
    a = int(num)

    if a == 1:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        addition = np.add(b,c)
        print("\nAdded values: \n", addition)
    elif a == 2:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        subtraction = np.subtract(b,c)
        print("\nSubtracted values: \n", subtraction)
    elif a == 3:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        multiply = np.multiply(b,c)
        print("\nMultiplied values", multiply)
    elif a == 4:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        divide = np.divide(b,c)
        print("\nDivided values", divide)
    elif a == 5:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        power = np.power(b,c)
        print("\nPower values", power)
    elif a == 6:
        num1 = input()
        num2 = input()
        b = int(num1)
        c = int(num2)
        modulus = np.mod(b,c)
        print("\nModulus values", modulus)




    elif a == 12:
        in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
        print ("Input array : \n", in_array)
        
        tan_Values = np.tan(in_array)
        print ("\nTan values : \n", tan_Values)
    elif a == 13:
        in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
        print ("Input array : \n", in_array)
        
        sin_Values = np.sin(in_array)
        print ("\nSin values : \n", sin_Values)
    elif a == 14:
        in_array = [0, np.pi / 4, 3*np.pi / 2, np.pi/6]
        print ("Input array : \n", in_array)
        
        cos_Values = np.cos(in_array)
        print ("\nCos values : \n", cos_Values)
    else:
        break