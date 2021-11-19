import sys
if len(sys.argv) < 4:
    print(f"Enter all data (workingout, amount, premium)")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    salary = a * b + c
    print(salary)


