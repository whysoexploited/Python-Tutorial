import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())


df = pd.read_csv('data.csv')
df.dropna(inplace = True)

print(df.to_string())

df.fillna(130, inplace = True)

df.fillna({"Calories": 130}, inplace=True)

x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].median()
df.fillna({"Calories": x}, inplace=True)

x = df["Calories"].mode()[0]

df.fillna({"Calories": x}, inplace=True)

