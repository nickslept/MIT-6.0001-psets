# Part B

annual_salary = float(input("Enter your salary: "))
portion_saved = float(input("Enter portion saved: "))
total_cost = float(input("Enter the cost of the house: "))
semi_annual_raise = float(input("Enter the semi-annual raise: "))

monthly_salary = annual_salary/12
months = 0
portion_down_payment = 0.25 
current_savings = 0.0
r = .04
savings_return = 0.0

while(((total_cost*portion_down_payment) - current_savings) > 0.0):
    months += 1
    savings_return = current_savings*r/12
    current_savings += (monthly_salary*portion_saved)+savings_return
    if (months%6==0):
        annual_salary += annual_salary*semi_annual_raise
        monthly_salary = annual_salary/12

print("Number of months: " + str(months))

