import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load CSV files
orders = pd.read_csv(r'C:\Users\ASUS\Documents\Project 1\orders.csv')
returns = pd.read_csv(r'C:\Users\ASUS\Documents\Project 1\returns.csv')

# Preview the datasets
print("Orders Data:")
print(orders.head())

print("\nReturns Data:")
print(returns.head())

# Drop missing values and duplicates
orders.dropna(inplace=True)
returns.dropna(inplace=True)
orders.drop_duplicates(inplace=True)
returns.drop_duplicates(inplace=True)

# Convert date columns to datetime
orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
returns['return_date'] = pd.to_datetime(returns['return_date'], errors='coerce')

# Drop invalid dates
orders.dropna(subset=['order_date'], inplace=True)
returns.dropna(subset=['return_date'], inplace=True)

# Ensure product_id is string
orders['product_id'] = orders['product_id'].astype(str)
returns['product_id'] = returns['product_id'].astype(str)

# Merge datasets
merged = pd.merge(orders, returns, on='order_id', how='left')

# Add return flag
merged['is_returned'] = merged['return_date'].notnull().astype(int)

# Preview merged data
print("\nMerged Data:")
print(merged.head())

# Save merged data
merged.to_csv(r'C:\Users\ASUS\Documents\Project 1\merged_orders_returns.csv', index=False)
print("\nMerged data saved successfully!")

# --- Return Rate Analysis ---
def calculate_return_rate(df, group_col):
    result = df.groupby(group_col)['is_returned'].mean().reset_index()
    result.columns = [group_col, 'return_rate (%)']
    result['return_rate (%)'] = result['return_rate (%)'] * 100
    return result

# Analyze return rate by group
if 'category' in merged.columns:
    print("\nReturn Rate by Category:")
    print(calculate_return_rate(merged, 'category'))

if 'supplier' in merged.columns:
    print("\nReturn Rate by Supplier:")
    print(calculate_return_rate(merged, 'supplier'))

if 'region' in merged.columns:
    print("\nReturn Rate by Region:")
    print(calculate_return_rate(merged, 'region'))

if 'marketing_channel' in merged.columns:
    print("\nReturn Rate by Marketing Channel:")
    print(calculate_return_rate(merged, 'marketing_channel'))

# --- Predictive Model: Logistic Regression ---
# Select features and target
features = merged[['price', 'category', 'supplier']]
target = merged['is_returned']

# One-hot encode categorical features
features_encoded = pd.get_dummies(features)

# Split data
X_train, X_test, y_train, y_test = train_test_split(features_encoded, target, test_size=0.3, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict return probabilities
merged['return_probability'] = model.predict_proba(features_encoded)[:, 1]

# Display top rows with high return probability
print("\nTop rows by return probability:")
print(merged[['order_id', 'return_probability']].sort_values(by='return_probability', ascending=False).head())

# Define threshold for high-risk products
high_risk = merged[merged["return_probability"] > 0.5]

# Save to CSV
high_risk.to_csv(r'C:\Users\ASUS\Documents\Project 1\high_risk_products.csv', index=False)

merged.to_csv(r'C:\Users\ASUS\Documents\Project 1\merged_orders_with_risk.csv', index=False)

