# Project 2: Cloud Hosting Cost Calculator

# Cost of one server per hour
cost_per_hour = 0.51

# Calculate costs
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# Calculate how many days a server can run with $918
budget = 918
days_with_budget = budget / cost_per_day

# Display the results
print("Cloud Hosting Cost Calculator")
print("--------------------------------")
print("Cost to operate one server per day   : $", round(cost_per_day, 2))
print("Cost to operate one server per week  : $", round(cost_per_week, 2))
print("Cost to operate one server per month : $", round(cost_per_month, 2))
print("Number of days one server can run with $918 :", round(days_with_budget, 2))