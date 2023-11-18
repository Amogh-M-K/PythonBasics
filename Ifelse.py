print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size of pizza do you want to order: S or M or L")
add_pepperoni = input("Do you want to add extra pepperoni: Y or N")
total_bill = 0
if size == "S":
    total_bill += 15
    print(f"You have to pay {total_bill}")
    if add_pepperoni == "Y":
        total_bill +=2
    print(f"Your bill is {total_bill}")
elif size == "M":
    total_bill = 20
    if add_pepperoni == "Y":
        total_bill += 3
    print(f"Your bill is {total_bill}")
elif size == "L":
    total_bill = 25
    add_pepperoni == "Y"
    total_bill +=3
    print(f"Your bill is {total_bill}")
add_cheese = input("Do you want an extra slice of cheese: Y or N")
if add_cheese == "Y":
  total_bill +=1
print(f"Your bill is {total_bill}")