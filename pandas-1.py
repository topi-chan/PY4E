
import pandas as pd
df = pd.read_csv("https://sololearn.com/uploads/files/titanic.csv")
small_df = df[["Age", "Sex", "Survived"]]
#print(small_df.head())
#df["male"] = df["Sex"] == "male"
#print(df.head())
print(df["Fare"].values)
