# Initial variable to track game play
player = "z"

# While we are still playing...
while player == "z":

    # Ask the user how many numbers to loop through
    player_number = int(input("How many numbers?"))

    # Loop through the numbers. (Be sure to cast the string into an integer.)
    for x in range(player_number):

        # Print each number in the range
        print(x)

    # Once complete...
    player= input("Continue: (y)es or (n)o?")