# initialize list of names for user input
names = []

# Note that the i is unused and could be replaced by an _
for i in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]

# @TODO: Use a list comprehension to create a list of titlecased names from the
# lowercased names. Reference: https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in lowercased]

# Print the invitations
invitations = [f"Dear {name}, please come to our halloween party this Saturday!" for name in titlecased]
for invitation in invitations:
    print(invitation)
