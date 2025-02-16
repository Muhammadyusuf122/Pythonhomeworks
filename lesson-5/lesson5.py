temperature= input(int("Enter a temperature in degrees Celcious:"))
convert_cel_to_far= (temperature* 9 / 5) +32
print(f"{temperature} degrees Celcious is {convert_cel_to_far} degrees Fahrenheit.")


temperature2=input(int("Enter a temperature in degrees Fahrenheit:"))
convert_far_to_cel=(temperature2-32)*5 / 9
print(f"{temperature2} degrees Fahrenheit is {convert_far_to_cel} degrees Celcious.")