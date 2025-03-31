# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = []

# Pie List
pie_list = ["Pecan", "Apple Crisp", "Chocolate", "Crepe", "Cinnanmon Bun",
            "Blueberry", "Taro", "Cherry", "Berry", "Cheesecake"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

    # Show pie selection prompt
    print("---------------------------------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Chocolate, (4) Crepe, " +
          " (5) Cinnamon Bun, (6) Blueberry, (7) Taro, (8) Cherry, " +
          " (9) Berry, (10) Cheesecake ")

    pie_choice = input("Which would you like? ")

    # Add pie to the pie list
    pie_purchases.append(pie_choice)

    print("------------------------------------------------------------------------")

    # Inform the customer of the pie purchase
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

    # Provide exit option
    shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete
print("------------------------------------------------------------------------")
print("You purchased a total of " + str(len(pie_purchases)) + ".")
