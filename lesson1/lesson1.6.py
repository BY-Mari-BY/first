print("Good day")
run = int(input("What distance you've done?"))
goal = int(input("What is your goal?"))
days = 1
while run < goal:
    run = run * 1.1
    days += 1
print(f"You need {days} days")
