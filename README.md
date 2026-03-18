# Predictive Churn & Revenue-at-Risk Engine

<img width="649" height="859" alt="Dashboard 1 (6)" src="https://github.com/user-attachments/assets/1fa7fa81-b5c5-40c3-9397-63e5b7304fc9" />


[![Tableau](https://img.shields.io/badge/Tableau-Live_Dashboard-blue?style=for-the-badge&logo=tableau)](https://public.tableau.com/views/PredictiveChurnRevenue-at-RiskEngineTelecoData/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
[![Python](https://img.shields.io/badge/Python-Scikit_Learn-yellow?style=for-the-badge&logo=python)](#)
[![Snowflake](https://img.shields.io/badge/Snowflake-SQL-lightgrey?style=for-the-badge&logo=snowflake)](#)

## 📌 Executive Summary
Customer acquisition is expensive, but customer retention is profitable. This project is an end-to-end machine learning and business intelligence pipeline designed to forecast customer churn and quantify the exact financial impact of departing accounts. 

By identifying high-risk customers before they cancel, this system provides the Customer Success team with a prioritized intervention roster to protect Annual Recurring Revenue (ARR).

👉 **[View the Live Interactive Tableau Dashboard Here]([INSERT_YOUR_TABLEAU_PUBLIC_LINK_HERE])**

## 🚀 Key Business Impact
* **Cloud Data Engineering:** Engineered a cloud-based ETL pipeline in **Snowflake (SQL)** to extract and transform raw subscription records into a clean Analytical Base Table, optimizing the data schema for machine learning ingestion.
* **Predictive Analytics:** Developed a Random Forest classification model using **Python (Scikit-Learn)** to calculate individual customer churn probabilities, successfully isolating the top three financial drivers of contract cancellation.
* **Business Intelligence & Strategy:** Designed an executive-facing **Tableau** decision-support dashboard that translated ML probability scores into a quantified "Revenue-at-Risk" metric, providing the sales team with a dynamic, prioritized intervention roster.

## 🧠 Strategic Insights
The machine learning model identified that **73% of the decision to churn** is driven by three key factors:
1. **Monthly Charges (27%)**: High price sensitivity among specific cohorts.
2. **Total Charges (26%)**: Cumulative spend threshold fatigue.
3. **Tenure (20%)**: A critical "flight risk" window during the first 10 months of the customer lifecycle.

*Recommendation:* Reallocate retention budgets to target accounts within their first year who are paying above the median monthly rate, utilizing the dashboard's "Target Hit List" for direct outreach.

## 🏗️ Technical Architecture
1. **Data Warehouse:** Raw data loaded and structured within **Snowflake**.
2. **Feature Engineering:** **SQL** used to handle nulls, encode target variables, and aggregate behavioral metrics.
3. **Machine Learning:** **Python (Pandas, Scikit-Learn)** utilized for one-hot encoding, train/test splitting, and training a Random Forest Classifier. `predict_proba()` applied to generate continuous risk scores.
4. **Data Visualization:** Output integrated into **Tableau** to build the "Flight Risk" matrix and executive BANs.

---
*Created by [Andy Machorro]([INSERT_YOUR_LINKEDIN_URL_HERE]) | Data Analyst*
