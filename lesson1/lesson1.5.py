print("Good day")
inc = int(input("Tell me your income"))
cost = int(input("Tell me your costs"))
if inc > cost:
    print("Congratulations!")
    profit = (inc - cost) / inc
    print(f"Profit: {profit}")
    empl_num  = int(input("Number of workers"))
    pr_per_empl = (inc - cost) / empl_num
    print(f"Profit per employer: {pr_per_empl}")
elif inc < cost:
    print("It's gonna be another day!")
elif inc == cost:
    print("Your result is 0")
print("Thank you. Good bye")
