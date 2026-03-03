# Below, I assigned variables to store the current total amount of money and the number of friends contributing to it.
current_total = 0
no_of_friends = 5

# Below, I assigned variables to store the cost of each category of food and drinks that we plan to order for the dinner date.
appetizers = 29.94
main_courses = 61.23
desserts = 43.56
drinks = 23.59

# Below, I calculated the total cost of the food and drinks by adding up the costs of each category.
current_total = appetizers + main_courses + desserts + drinks
print('Total cost so far:', current_total)

# A tip of 10% of the current total was added due to excellent service. I then calculated the new total by adding the tip amount using the augmented assignment operator. Finally, I printed the total cost including the tip.
tip = current_total * 0.10
current_total += tip
print('Total cost with tip:', current_total)

# Finally, I calculated the amount each friend needs to contribute by dividing the current total by the number of friends. I then printed the amount each friend needs to pay.
bill_per_friend = current_total / no_of_friends
print('Bill per friend:', bill_per_friend)

#Since the amount include cents, we need to round off the amount figure accurate to 2 decimal places using the round() function. Finally, I printed the amount each friend needs to pay.
each_pays = round(bill_per_friend, 2)
print('Each friend pays:', each_pays)