# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
# Analyze and visualize the top 10 association rules by lift
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset creation (for illustration, you can load your dataset instead)
data = pd.DataFrame([
    [1, 1, 0],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
], columns=['Milk', 'Bread', 'Butter'])

# Display the dataset
print("Dataset:")
print(data)

# Ensure the data is in the correct boolean format (1 for True, 0 for False)
data = data.astype('bool')

# Apply the Apriori algorithm to find frequent itemsets
# Set the minimum support threshold (e.g., 50%)
min_support = 0.5
frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)

# Display the frequent itemsets
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules from the frequent itemsets
# Set the minimum confidence threshold (e.g., 20%)
min_confidence = 0.2
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Display the association rules
print("\nAssociation Rules:")
print(rules)


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
