# PART C

semi_annual_raise = .07
r = .04
down_payment = .25
total_cost = 1000000
annual_salary = int(input("Enter the base salary (annual):"))

possible = True
high = 10000
low = 0
steps = 0
tolerance = 100

def run_simulation(guess, annual_salary):
    #initializing variables
    current_savings = 0.0
    savings_return = 0.0
    monthly_salary = int(annual_salary/12)
    current_salary = annual_salary

    for month in range (1,37,1): #monthly simulation
        savings_return = current_savings*r/12
        current_savings += monthly_salary*(round((.0001*guess),4)) + savings_return
        if (month%6==0): #raise every 6 months
            current_salary += current_salary*semi_annual_raise
            monthly_salary = current_salary/12
    
    return total_cost*down_payment - current_savings #returns money needed after downpayment (e.g. -200 = you saved 200 more than the required downpayment)

while(high-low>1):
    steps+=1
    guess=int((high+low)/2)
    if run_simulation(guess, annual_salary) < -tolerance: #saved too much
        high = guess
    elif run_simulation(guess, annual_salary) > tolerance: #saved too little
        low = guess
        if(guess>=9999): 
            possible = False

if(possible):
     print("Rate: " + str(guess*.01))
     print("Steps: " + str(steps))
else:
     print("Not possible")



# bi_steps = 0
# low = 0
# high = 10000
# epsilon = 100.0 
# guess = (high+low)/2.0
# possible = True
# current_annual_salary = annual_salary
# current_savings = 0
# monthly_salary = annual_salary/12
# months = 0
# while(high-low > 1):
#     bi_steps+=1
#     guess = int((high+low)/2.0)
#     money_left = run_simulation(guess)
#     if(money_left < -epsilon):
#         print("low", str(guess), "savings:", str(money_left)) #test
#         high = guess
#         current_savings = 0
#         current_annual_salary = annual_salary
#         monthly_salary = annual_salary/12
#     elif(guess >= 9999 and money_left > epsilon):
#         possible = False
#         break
#     elif(money_left > epsilon):
#         print("high", str(guess), "savings:", str(total_cost*down_payment-current_savings)) #test
#         low = guess
#         current_savings = 0
#         current_annual_salary = annual_salary
#         monthly_salary = annual_salary/12
#     else:
#         break
        
# if(possible):
#     print("Rate: " + str(guess*.01))
#     print("money left:" + str(money_left))
#     print("Steps: " + str(bi_steps))
#     print("high" + str(high))
#     print("low" + str(low))
# else:
#     print("Not possible")
