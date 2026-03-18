# IBM Telco Customer Predictive Churn & Revenue-at-Risk Engine

<img width="649" height="859" alt="Dashboard 1 (6)" src="https://github.com/user-attachments/assets/1fa7fa81-b5c5-40c3-9397-63e5b7304fc9" />


[![Tableau](https://img.shields.io/badge/Tableau-Live_Dashboard-blue?style=for-the-badge&logo=tableau)](https://public.tableau.com/views/PredictiveChurnRevenue-at-RiskEngineTelecoData/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
[![Python](https://img.shields.io/badge/Python-Scikit_Learn-yellow?style=for-the-badge&logo=python)](https://github.com/amachorro773-a11y/Predictive-Churn-Revenue-at-Risk-Engine-/blob/main/telco_cust_churn.py)
[![Snowflake](https://img.shields.io/badge/Snowflake-SQL-lightgrey?style=for-the-badge&logo=snowflake)](https://docs.google.com/document/d/1uw4_8KN8PFx2trNOmuHj7WuJ0n_GkJzpqbFk7lKnWBU/edit?tab=t.0)

## 📌 Executive Summary
Customer acquisition is expensive, but customer retention is profitable. So I implemented an end-to-end machine learning and business intelligence pipeline designed to forecast customer churn and quantify the exact financial impact of departing accounts. 

By identifying high-risk customers before they cancel, this system provides the Customer Success team with a prioritized intervention roster to protect Annual Recurring Revenue (ARR).

👉 **[View the Live Interactive Tableau Dashboard Here]([INSERT_YOUR_TABLEAU_PUBLIC_LINK_HERE])**

## 🚀 Key Business Impact
* Built a cloud-based ETL pipeline in **Snowflake (SQL)** to extract and transform raw subscription records into a clean Analytical Base Table, optimizing the data schema for machine learning ingestion.
* Trained a Random Forest classification model using **Python (Scikit-Learn)** to calculate individual customer churn probabilities. Translated these probabilities into a quantified "Revenue-at-Risk" metric by multiplying the risk score by the account's monthly contract value.
* A probability threshold of **75%** was selected to prioritize precision over recall in high-cost intervention scenarios.

## 🧠 Model Evaluation & Trade-Offs
* **Algorithm Selection:** Selected a **Random Forest Classifier** over Logistic Regression to effectively capture nonlinear relationships (e.g., the compounding effect of high prices and low tenure) without requiring heavy feature scaling or transformation.
* **Performance Metrics:** The baseline model achieved an **ROC-AUC score of 0.804** and an overall accuracy of **77%**. Because the business cost of a false negative (missing a churning customer) is higher than a false positive, analysis heavily weighed **Recall (0.47)** and **Precision (0.60)** for the minority class (Churn = 1).
* Identified inherent class imbalance within the dataset. Future iterations will test SMOTE (Synthetic Minority Over-sampling Technique) or adjusted class weights to further optimize recall for high-value accounts.


<img width="800" height="600" alt="Screenshot 2026-03-18 at 11 45 57 AM" src="https://github.com/user-attachments/assets/01e27038-923e-4522-94dd-b67c7cb765b3" />

* The model achieved an **Average Precision (AP) of 0.58**, reflecting moderate discriminative ability under class imbalance.
* To determine an appropriate decision boundary, I analyzed the Precision-Recall curve and evaluated F1 scores across probability thresholds. The mathematically optimal F1 score occurred at a threshold of **0.28**, maximizing the harmonic balance between Precision and Recall.
* However, threshold selection was guided by operational constraints rather than pure mathematical optimization.
* At a **0.28** threshold, recall increases but precision declines substantially — resulting in a large number of false positives. This could overwhelm the retention team with low-confidence outreach and reduce the ROI of discount interventions.
* To align the model with business capacity and cost structure, the intervention threshold was raised to **0.75**, prioritizing high Precision over Recall. This ensures that retention resources are concentrated on the highest-confidence churn risks, improving efficiency and maximizing expected return on intervention efforts.
  

## 📊 Feature Importance Insights
The model's feature importance analysis (Mean Decrease in Impurity) indicated that three variables represented **73% of total feature importance weight (Mean Decrease in Impurity):**
1. **Monthly Charges (27%)**: High price sensitivity among specific cohorts.
2. **Total Charges (26%)**: Cumulative spend threshold fatigue.
3. **Tenure (20%)**: A critical "flight risk" window during the first 10 months of the customer lifecycle.

*Recommendation:* Reallocate retention budgets to target accounts within their first year who are paying above the median monthly rate.

---
*Created by [Andy Machorro]([INSERT_YOUR_LINKEDIN_URL_HERE]) | Data Analyst*
