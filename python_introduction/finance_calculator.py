income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))


monthly_savings = income - expenses


annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)


print("Your monthly savings are", "$", monthly_savings)
print("Projected savings after one year, is:", "$", projected_savings)
