name = input("Employee Name: ")
time = int(input("Enter number of hours: "))
SSS = float(input("SSS contribution: "))
PH = float(input("Phil health: "))
House = float(input("House loan: "))
RPH = 500



print("""
      ==========PAYSLIP==========
==========EMPLOYEE INFORMATION==========
""")
print("Employee name:", name.upper())
print("Rendered hour:", time)
print("Rate per hour:", RPH)
GS = time * RPH
print("Gross Salary:", GS)
print("\n==========DEDUCTIONS==========")
print("SSS:", SSS)
print("PhilHealth:", PH)
print("Other loan:", House)
Tax = GS/time
print("Tax:", Tax)
TD = SSS + PH + House + Tax
print("Total Deductions:", TD)

NS = GS - TD
print("\nNet salary: PHP", NS)
