name=input()
print(f"{name[0]}.{name[5]}")


name=input("პროდუქტის სერიული ნომერი:")
first3=name[:3]
last3=name[-3:]
print(f"{first3}{last3}")


password=input("შეიყვანეთ პაროლი")
first_letter=password[0]
last_letter=password[-1]
print(f"{password[0]}{password[-1]}")
