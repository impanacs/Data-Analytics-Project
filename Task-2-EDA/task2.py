import pandas as pd
df = pd.read_csv("Task-2-EDA/Student_EDA.csv")
print(df.head())
print(df.shape) #default 5 first rows
print(df.info())

print("Mean:")
print(df.mean(numeric_only=True))

print("\nMedian:")
print(df.median(numeric_only=True))

print("\nMode:")
print(df.mode(numeric_only=True).iloc[0]) #integer location (index no 0,frst row)
print("\nStandard Deviation:")
print(df.std(numeric_only=True))

# visualization
# histogram
import matplotlib.pyplot as plt
plt.hist(df["Overall_Performance"], bins=10)#intervals
plt.xlabel("Overall Performance")
plt.ylabel("Number of Students")
plt.title("Distribution of Overall Performance")
plt.show()

#Boxplot
plt.boxplot(df["Overall_Performance"])
plt.ylabel("Overall Performance")
plt.title("Boxplot of Overall Performance")
plt.show()

# Scatter Plot
plt.scatter(df["Study_Hours_Per_Day"],df["Overall_Performance"])
plt.xlabel("Study Hours Per Day")
plt.ylabel("Overall Performance")
plt.title("Study Hours vs Overall Performance")

plt.show()

# correlation
correlation = df.corr(numeric_only=True)
print(correlation)

import seaborn as sns
import matplotlib.pyplot as plt
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

corr = df.corr(numeric_only=True)
#remove duplicates values from matrix
upper = corr.where(
    __import__("numpy").triu(__import__("numpy").ones(corr.shape),k=1).astype(bool)
)
strongest = upper.stack().sort_values(key=abs, ascending=False)
print(strongest.head(10))