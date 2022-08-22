#Title: foodCheck.py
#Author: Grant Andrews
#Date: 1/26/2022
#Description: This program asks the user how much their drinks, apetizer,
# and entree costs, then calculates the grand total of their bill, including
# a tip of 18% and a tax of 4.75%.


drinks = float(input("How much did your drinks cost? \n $ "))                       # Ask the user how much their drinks cost, and assign user input to variable "drinks".
apetizer = float(input("How much did your apetizer cost? \n $ "))                   # Ask the user how much their apetizer cost, and assign user input to variable "apetizer".
entree = float(input("How much did your entree cost? \n $ "))                       # Ask the user how much their entree cost, and assign user input to variable "entree".
tax, tip, meal = .0475, .18, drinks + apetizer + entree                             # Assign the variables "tax", "tip", and "meal", where "tax" = 4.75%, "tip" = 18%, and "meal" = "drinks" + "apetizer" + "entree".
calculated_tax, calculated_tip = tax * meal, tip * meal                             # Calculates the tax and tip based on the cost of the meal, and assigns values to variables "calculated_tax", and "calculated_tip".
total = meal + calculated_tip + calculated_tax                                      # Calculates the total for the meal by adding the "calculated_tip", "calculated_tax", and "meal" variables, assigns this value to variable "total".
print ("The total for your meal, including tax and a tip comes to $",
       format(total, ".2f"))                                                        # Prints the total cost of the meal to the user, using variable "total".