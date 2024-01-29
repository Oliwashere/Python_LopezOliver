## -------------------------------
## ------- EJERCICIO 1 -----------
## -------------------------------

# ---- Money Change ----

def min_coins(money, coins):
    # Initialize an array to store the minimum number of coins needed for each value up to money
    coins_needed = [float('inf')] * (money + 1)
    coins_needed[0] = 0
    
    # Fill the coins_needed array using a loop
    for i in range(1, money + 1):
        # For each coin denomination
        for coin in coins:
            # If the coin denomination is less than or equal to the current value
            if coin <= i:
                # Update the minimum number of coins needed for the current value
                coins_needed[i] = min(coins_needed[i], coins_needed[i - coin] + 1)
    
    # Return the minimum number of coins needed to change money
    return coins_needed[money] if coins_needed[money] != float('inf') else -1

# Get the amount from the user
amount = int(input(""))

# Test the function with the user-provided amount
coins = [1, 5, 10]
print(min_coins(amount, coins))

## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715