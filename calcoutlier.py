import pandas as pd

# Load the dataset
file_path = 'datasets/loan_data.csv'
df = pd.read_csv(file_path)

# Calculate Q1, Q3, and IQR for interest rates in 'debt_consolidation'
Q1 = df[df['purpose'] == 'debt_consolidation']['int.rate'].quantile(0.25)
Q3 = df[df['purpose'] == 'debt_consolidation']['int.rate'].quantile(0.75)
IQR = Q3 - Q1

# Calculate lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers in 'debt_consolidation'
debt_consolidation_outliers = df[(df['purpose'] == 'debt_consolidation') & 
                                 ((df['int.rate'] < lower_bound) | 
                                  (df['int.rate'] > upper_bound))]

# Remove the outliers from the dataset
df_cleaned = df.drop(debt_consolidation_outliers.index)

# Display the shape of the cleaned DataFrame to confirm the removal
df_cleaned.shape
