celsius=int(input("შეიყვანეთ ტემპერატურა:"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C არის {fahrenheit}°F")


weight = float(input("შეიყვანეთ წონა:"))
height = float(input("შეიყვანეთ სიმაღლე: "))
BMI= weight / (height ** 2)
print(BMI)


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
total_sum = num1 + num2 + num3 + num4 + num5
print(total_sum)



num1 = int(input())
num2 = int(input())
num3 = int(input())


count=(num1>100)+(num2>100)+(num3>100)
print(f"ასზე მეტი არის {count} რიცხვი")