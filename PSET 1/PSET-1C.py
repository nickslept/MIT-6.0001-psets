# PART C

semi_annual_raise = .07
r = .04
down_payment = .25
total_cost = 1000000
annual_salary = float(input("Enter the base salary:"))
curr_annual_salary = annual_salary
current_savings = 0
monthly_salary = annual_salary/12
months = 0

def run_simulation(guess):
    for month in range (1,37,1):
        savings_return = current_savings*r/12
        current_savings += monthly_salary*(round((.0001*guess),4))+savings_return
        if (month%6==0):
            curr_annual_salary += curr_annual_salary*semi_annual_raise
            monthly_salary = curr_annual_salary/12
    return total_cost*down_payment - current_savings 


bi_steps = 0
low = 0
high = 10000
epsilon = 100.0 
guess = (high+low)/2.0
possible = True

while(high-low > 1):
    bi_steps+=1
    guess = int((high+low)/2.0)
    money_left = run_simulation(guess)
    if(money_left < -epsilon):
        print("low", str(guess), "savings:", str(money_left)) #test
        high = guess
        current_savings = 0
        curr_annual_salary = annual_salary
        monthly_salary = annual_salary/12
    elif(guess >= 9999 and money_left > epsilon):
        possible = False
        break
    elif(money_left > epsilon):
        print("high", str(guess), "savings:", str(total_cost*down_payment-current_savings)) #test
        low = guess
        current_savings = 0
        curr_annual_salary = annual_salary
        monthly_salary = annual_salary/12
    else:
        break
        
if(possible):
    print("Rate: " + str(guess*.01))
    print("money left:" + str(money_left))
    print("Steps: " + str(bi_steps))
    print("high" + str(high))
    print("low" + str(low))
else:
    print("Not possible")
