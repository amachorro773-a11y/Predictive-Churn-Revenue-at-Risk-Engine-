import snowflake.connector
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

print("connecting to snowflake")
conn = snowflake.connector.connect(
    user = "ANDY",
    password='Coolbeans03***',
    account = "PANWYQP-WFB59220", 
    warehouse='COMPUTE_WH',            
    database='PORTFOLIO_DB',
    schema='CHURN_PROJECT'
)

# SQL query to grab table
query = """
    SELECT * FROM PORTFOLIO_DB.CHURN_PROJECT.ABT_CHURN_FEATURES;
"""

# Extract the data directly into a Pandas DataFrame
print("Extracting Analytical Base Table...")
df = pd.read_sql(query, conn)
conn.close()
print("\nExtraction Successful! Here are the first 5 rows:")
print(df.head())

# --- MACHINE LEARNING PREPROCESSING ---
print("\nPreparing data for the Machine Learning Model...")

# Drop the 11 brand new customers who have blank Total Charges
df.dropna(inplace=True)

# Separate the ID and Target Variable from the features we will use to predict
X = df.drop(columns=['CUSTOMER_ID', 'CHURN_STATUS'])
y = df['CHURN_STATUS']

# One-Hot Encoding: Convert all text columns into 1s and 0s
X_encoded = pd.get_dummies(X, drop_first=True)

# Verify the translation worked
print(f"Original columns: {len(X.columns)} -> Encoded columns: {len(X_encoded.columns)}")
print("\nHere is what the Machine Learning model will actually 'see':")
print(X_encoded.head())



print("\n--- TRAINING THE PREDICTIVE MODEL ---")

# Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize and Train the Random Forest
print("Training the Random Forest algorithm...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Grade the Model's Homework
print("\nGrading the Model (Classification Report):")
predictions = rf_model.predict(X_test)
print(classification_report(y_test, predictions))

# The Business Value: Feature Importance
# This tells the CFO exactly what drives customers to cancel
importances = pd.Series(rf_model.feature_importances_, index=X_encoded.columns)
print("\n--- TOP 3 DRIVERS OF CUSTOMER CHURN ---")
print(importances.sort_values(ascending=False).head(3))


# --- EXPORTING THE BUSINESS VALUE  ---
print("\nGenerating Churn Probability Scores for all customers...")

# Calculate the exact probability of churning (Class 1)
# [:, 1] grabs the probability of the '1' column specifically
df['CHURN_PROBABILITY_SCORE'] = rf_model.predict_proba(X_encoded)[:, 1]

# Calculate Expected Revenue at Risk (Monthly Bill * Probability of Leaving)
df['REVENUE_AT_RISK'] = df['MONTHLY_CHARGES'] * df['CHURN_PROBABILITY_SCORE']

# Sort the dataframe to show the highest risk customers at the top
df_final = df.sort_values(by='CHURN_PROBABILITY_SCORE', ascending=False)

# Export the clean, scored data to a CSV file for Tableau
df_final.to_csv('Churn_Predictions_for_Tableau.csv', index=False)

print("\nSUCCESS! Check your project folder for 'Churn_Predictions_for_Tableau.csv'")
