import pandas as pd
df = pd.read_csv("Employee_data.csv")
print(df.head()) #df DataFrame, #head() displays first 5 rows by default
print(df)
print(df.head(50))
print(df.info()) # gives info abt df
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df.duplicated().sum())
df = df.drop_duplicates()

df["Gender"] = df["Gender"].replace({
    "M" : "Male",
    "male" : "Male",
    "MALE": "Male",
    "F" : "Female",
    "female": "Female"
})
df["City"] = df["City"].replace({
    "Bangalore":"Bengaluru",
    "bengaluru" : "Bengaluru",
    "MYSORE" : "Mysore"
})
df["Join_Date"] = pd.to_datetime(df["Join_Date"], errors="coerce")
df["Join_Date"] = df["Join_Date"].dt.strftime("%Y-%m-%d")
df.to_csv("cleaned_Employee_data.csv", index = False)


print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDulicate Rows After Cleaning:")
print(df.isnull().sum())

print("\nFirst 5 Rows of Cleaned Data:")
print(df.head())

print("\nData Cleaning Completed Successfully!")