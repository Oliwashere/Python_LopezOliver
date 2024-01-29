## -------------------------------
## ------- EJERCICIO 1 -----------
## -------------------------------

# ---- Money Change ----

def min_coins(money):
    dp = [0] + [float('inf')] * money
    for i in range(1, money + 1):
        dp[i] = min(dp[i - 1], dp[i - 5] + (i - 5) // 5, dp[i - 10] + (i - 10) // 10)
    return dp[money] if dp[money] != float('inf') else -1
    


## Desarrollado por OLIVER EDUARDO LOPEZ PEREZ - 1097911715