# Take input of you and your neighbor
your_name = input("What is your name?")

neighbor_name = input("what is your neighbor's name?")
# Take how long each of you have been coding
you_code= input(" How many months have you've been coding?")

neighbor_code = input("how many months has your neighbor been coding?")
# Add total month
total_months = int(you_code) + int(neighbor_code)
# Print results
print("I am " + your_name + " and my neighbor is " + neighbor_name)
print("Together we have been coding for " + str(total_months) + " months!")
