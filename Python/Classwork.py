'''
The cost for making 5 pieces momo is Rs. 24 and Rs. 2.35 for 50ml of sauce. The cost for rent is Rs. 5.65 per plate and service charge for a waiter is Rs. 17 per plate. If a customer pays Rs. 65 for a plate of momo (10 pieces and 30ml sauce) find the total profit or loss percentage.
'''
cost_momo=round(24/5,2)
cost_sauce=round(2.35/50,2)
cost_waiter=round(17/10,2)
cost_rent=round(5.65/10,2)
total_income=65
total_cost= 10*cost_momo+30*cost_sauce+cost_rent*10+cost_waiter*10
if total_income>total_cost:
    profitpercetage=round((total_income-total_cost)/total_cost * 100,2)
    print(f"The profit percentage is {profitpercetage}%")

elif total_income<total_cost:
    losspercetage=round((total_cost-total_income)/total_cost * 100,2)
    print(f"The loss percentage is {losspercetage}%")
else:
    print("Its breakeven")