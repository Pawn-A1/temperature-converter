a = input("What are you converting? (C, F, K) ")

if a == "C": 
    degrees_C = float(input("How many Celsius? "))
    degrees_C_to_F = round(((9/5) * degrees_C + 32), 2)
    degrees_C_to_K = degrees_C + 273.15
    print(str(degrees_C)+" celsusis is "+str(degrees_C_to_F)+" fahrenheit and "+str(degrees_C_to_K)+" kelvin")
elif a == "F":
    degrees_F = float(input("How many Fahrenheit? "))
    degrees_F_to_C = round(5/9*(degrees_F-32), 2)
    degrees_F_to_K = round((5/9*(degrees_F-32)+273.15), 2)
    print(str(degrees_F)+" degrees Fahrenheit is "+str(degrees_F_to_C)+" degrees Celsius and "+str(degrees_F_to_K)+" degrees Kelvin")
elif a == "K":
    degrees_K = float(input("How many Kelvin? "))
    degrees_K_to_C = degrees_K-273.15
    degrees_K_to_F = round((9/5*(degrees_K-273.15)+32), 2)
    print(str(degrees_K)+" degrees Kelvin is "+str(degrees_K_to_C)+" degrees Celsius and "+str(degrees_K_to_F)+" degrees Fahrenheit")
else:
    print("please choose a valid format (C, F or K) ")

input("Press enter to exit")