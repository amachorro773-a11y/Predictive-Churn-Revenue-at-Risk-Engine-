import snowflake.connector
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

print("connecting to snowflake")
conn = snowflake.connector.connect(
    user = "ANDY",
    password='Coolbeans03***',
    account = "PANWYQP-WFB59220", # e.g., 'xy12345.us-east-2.aws'
    warehouse='COMPUTE_WH',            # This is the default free warehouse
    database='PORTFOLIO_DB',
    schema='CHURN_PROJECT'
)

# 2. Write the SQL query to grab your engineered table
query = """
    SELECT * FROM PORTFOLIO_DB.CHURN_PROJECT.ABT_CHURN_FEATURES;
"""

# 3. Extract the data directly into a Pandas DataFrame
print("Extracting Analytical Base Table...")
df = pd.read_sql(query, conn)

# 4. Close the secure connection (Best Practice!)
conn.close()

# 5. Verify the data arrived safely
print("\nExtraction Successful! Here are the first 5 rows:")
print(df.head())

# --- MACHINE LEARNING PREPROCESSING ---
print("\nPreparing data for the Machine Learning Model...")

# 1. Drop the 11 brand new customers who have blank Total Charges
df.dropna(inplace=True)

# 2. Separate the ID and Target Variable from the features we will use to predict
X = df.drop(columns=['CUSTOMER_ID', 'CHURN_STATUS'])
y = df['CHURN_STATUS']

# 3. One-Hot Encoding: Convert all text columns into 1s and 0s
X_encoded = pd.get_dummies(X, drop_first=True)

# 4. Verify the translation worked
print(f"Original columns: {len(X.columns)} -> Encoded columns: {len(X_encoded.columns)}")
print("\nHere is what the Machine Learning model will actually 'see':")
print(X_encoded.head())



print("\n--- TRAINING THE PREDICTIVE MODEL ---")

# 1. The Train/Test Split (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# 2. Initialize and Train the Random Forest
print("Training the Random Forest algorithm...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 3. Grade the Model's Homework
print("\nGrading the Model (Classification Report):")
predictions = rf_model.predict(X_test)
print(classification_report(y_test, predictions))

# 4. The Business Value: Feature Importance
# This tells the CFO exactly what drives customers to cancel
importances = pd.Series(rf_model.feature_importances_, index=X_encoded.columns)
print("\n--- TOP 3 DRIVERS OF CUSTOMER CHURN ---")
print(importances.sort_values(ascending=False).head(3))


# --- EXPORTING THE BUSINESS VALUE (FOR TABLEAU) ---
print("\nGenerating Churn Probability Scores for all customers...")

# 1. Calculate the exact probability of churning (Class 1)
# [:, 1] grabs the probability of the '1' column specifically
df['CHURN_PROBABILITY_SCORE'] = rf_model.predict_proba(X_encoded)[:, 1]

# 2. Calculate Expected Revenue at Risk (Monthly Bill * Probability of Leaving)
df['REVENUE_AT_RISK'] = df['MONTHLY_CHARGES'] * df['CHURN_PROBABILITY_SCORE']

# 3. Sort the dataframe to show the highest risk customers at the top
df_final = df.sort_values(by='CHURN_PROBABILITY_SCORE', ascending=False)

# 4. Export the clean, scored data to a CSV file for Tableau
df_final.to_csv('Churn_Predictions_for_Tableau.csv', index=False)

print("\nSUCCESS! Check your project folder for 'Churn_Predictions_for_Tableau.csv'")