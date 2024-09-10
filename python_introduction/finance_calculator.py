monthly_income = int(input("Enter your Monthly Income? "))
monthly_expenses = int(input("Enter your Monthly Expenses? "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("YOur monthly savings is ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)