import pandas as pd
data = {"city": ["Kyiv", "Lviv", "Odesa"], "sales": [1200, 950, 500]}
df = pd.DataFrame(data)
print("Продажі по містах:")
print(df)
# Розрахунок середнього значення продажів
print("Середнє значення:", df["sales"].mean())