# Capstone Project: Predicting Customer Vehicle Purchase Preferences for a Toyota Dealership

## Overview
This project aims to predict which Toyota vehicle model (Camry, Corolla, RAV4, Prius, Tacoma, Highlander) a potential customer is most likely to purchase based on their demographic, behavioral, and financial characteristics. The insights from this analysis can help dealerships optimize inventory, target marketing, and improve personalized sales recommendations.

---

## Dataset
The dataset contains simulated Toyota customer data with the following columns:

`vehicle_model`, `msrp`, `sale_price`, `price_vs_msrp`, `age`, `gender`, `income`, `occupation`, `family_size`, `weekly_commute_miles`, `fuel_preference`, `test_drive_interest`, `loyalty_score`, `purchase_urgency`, `zip_code`, `median_zip_income`, `urban_rural`, `income_to_zip_ratio`

---

## Data Cleaning and Preparation
- Checked for missing values and duplicates.
- Imputed missing numeric values (`income`, `weekly_commute_miles`, `income_to_zip_ratio`) using the median.
- Filled categorical missing values for `occupation` (`None` or empty treated as “Other”) and `fuel_preference` (“No preference”).
- Cleaned categorical columns to remove trailing spaces.
- Removed duplicate rows.

**Visualizations:**
- Missing values per column:  
![Missing Values](images/missing_values_per_column.png)
- Vehicle model distribution:  
![Vehicle Models](images/vehicle_models.png)

---

## Feature Engineering
- **`is_family`**: Derived from `family_size`. `True` if family_size > 1, else `False`. This feature helps capture differences in vehicle preference between single customers and families.

**Visualizations for feature insights:**
- Income vs Vehicle Model:  
![Income vs Vehicle Models](images/income_vs_vehicle_models.png)
- Weekly Commute vs Vehicle Model:  
![Weekly Commute vs Vehicle Models](images/weekly_commute_vs_vehicle_models.png)
- Fuel Preference vs Vehicle Model:  
![Fuel Preference vs Vehicle Models](images/fuel_pref_vs_vehicle_models.png)

---

## Exploratory Data Analysis (EDA)
- Numeric feature distributions and outlier analysis performed using histograms and boxplots.
- Categorical feature distributions assessed via countplots.
- Bivariate analysis to examine relationships between numeric/behavioral features and vehicle choice.

---

## Baseline Model: Random Forest Classifier

**Why Random Forest?**  
- Handles numeric and categorical features.  
- Captures non-linear relationships between customer attributes and vehicle choice.  
- Robust to outliers in features like weekly commute distance.  
- Provides feature importance for business insights.  
- Strong baseline with reduced overfitting compared to a single decision tree.

**Evaluation Metric:**  
- **Accuracy** is the primary metric for this multi-class classification task.  
- **Precision, recall, and F1-score** are also reported to assess performance per vehicle model.


**Pipeline includes:**  
- Numeric transformer: median imputation + standard scaling  
- Categorical transformer: constant imputation + One-Hot Encoding  

**Baseline Performance:**
- Accuracy: 0.2400
- Classification report:

| Vehicle Model | Precision | Recall | F1-score | Support |
|---------------|-----------|--------|----------|---------|
| Camry         | 0.202     | 0.213  | 0.208    | 2089    |
| Corolla       | 0.179     | 0.120  | 0.143    | 1794    |
| Highlander    | 0.139     | 0.039  | 0.061    | 1187    |
| Prius         | 0.184     | 0.069  | 0.100    | 1279    |
| RAV4          | 0.280     | 0.571  | 0.376    | 2797    |
| Tacoma        | 0.089     | 0.009  | 0.017    | 854     |

**Confusion Matrix:**  
![Confusion Matrix](images/confusion_matrix_baseline_model.png)

---

## Feature Importance
Top 10 features influencing model prediction:

| Feature                   | Importance |
|----------------------------|------------|
| loyalty_score              | 0.115      |
| income                     | 0.114      |
| weekly_commute_miles       | 0.113      |
| income_to_zip_ratio        | 0.111      |
| age                        | 0.104      |
| median_zip_income          | 0.065      |
| family_size                | 0.040      |
| purchase_urgency_Browse    | 0.019      |
| purchase_urgency_3_months  | 0.018      |
| gender_Female              | 0.018      |

**Feature Importance Visualization:**  
![Feature Importance](images/Feature_importance_for_prediction.png)

---

## Summary and Next Steps
- Data cleaning and basic feature engineering completed. Dataset is ready for modeling.  
- Baseline Random Forest model provides a starting accuracy of 24%, which can be improved with feature selection, hyperparameter tuning, or alternative classification algorithms.  
- Visualizations highlight key relationships between customer characteristics and vehicle preferences.  
- **Next steps:** refine features, experiment with other classifiers, and evaluate using cross-validation to improve prediction performance.
