import numpy as np

stock_prices = np.random.randint(100, 500, size=(30, 5))

average = np.mean(stock_prices, axis=0)
print(average)

Highest_price = np.max(stock_prices)
max_index = np.unravel_index(np.argmax(stock_prices), stock_prices.shape)
Highest_Day = max_index[0] + 1
Company_Highest = max_index[1] + 1

print(f"Highest price record: {Highest_price} at Day {Highest_Day} and Company {Company_Highest}")

min_value = np.min(stock_prices)
max_value = np.max(stock_prices)
normalized_prices = np.round(stock_prices - min_value) / (max_value - min_value)
print(normalized_prices)

print("\nRisky Investment Days:")
for i, row in enumerate(stock_prices):
    risky = row[row < 200]
    if risky.size > 0:
        print(f"Day {i+1}: {risky.tolist()}")