salary_per_month = int(input('How much money do you earn per month?\n'))
my_salary = salary_per_month
sum_estimated = int (input('How much money would you want to save?\n'))
desired_sum = sum_estimated
expenses = int(input('What are your monthly expenses on life?\n'))
final_sum = my_salary - expenses
months = desired_sum / final_sum
years = desired_sum / final_sum / 12
print (f'you need {round(months)} months 1or  {round(years)} years to earn this sum of money')

