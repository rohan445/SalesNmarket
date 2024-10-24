# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load dataset from user input
def load_dataset():
    file_name = input("Enter the CSV file name (with extension): ")
    try:
        data = pd.read_csv(file_name)
        return data
    except FileNotFoundError:
        print("File not found. Please ensure the file is in the current directory and try again.")
        return None

# Function to get user inputs for support and confidence
def get_thresholds():
    min_support = float(input("Enter the minimum support threshold (e.g., 0.5 for 50%): "))
    min_confidence = float(input("Enter the minimum confidence threshold (e.g., 0.2 for 20%): "))
    return min_support, min_confidence

# Load dataset
data = None
while data is None:
    data = load_dataset()

# Display the dataset
print("Dataset:")
print(data.head())

# Ensure the data is in the correct boolean format (1 for True, 0 for False)
data = data.astype('bool')

# Get user-defined thresholds
min_support, min_confidence = get_thresholds()

# Apply the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)

# Display the frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Display the association rules
print("\nAssociation Rules:")
print(rules)

# Analyze and visualize the top 10 association rules by lift
# Sort rules by lift and display the top 10
top_rules = rules.sort_values(by='lift', ascending=False).head(10)
print("\nTop 10 Association Rules by Lift:")
print(top_rules)

# Plot the top 10 rules by lift
plt.figure(figsize=(10, 6))
sns.barplot(x='lift', y=top_rules.index, data=top_rules, orient='h')
plt.xlabel('Lift')
plt.ylabel('Rule Index')
plt.title('Top 10 Association Rules by Lift')
plt.show()
