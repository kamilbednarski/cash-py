from cs50 import get_float

# Getting user input as change value is US dollars
# Only positive number allowed.
while (True):
    change_value = 100 * get_float("Change owed: ")
    if change_value > 0:
        break

# Coin nominations for USD.
coin_nominations = [25, 10, 5, 1]


coin_counter = 0


# Calculating number of coins needed.
i = 0
for i in range(0, 4):
    while (change_value >= coin_nominations[i]):
        coin_counter += 1
        change_value -= coin_nominations[i]

# Printing result.
print("In total you need:")
print(coin_counter)