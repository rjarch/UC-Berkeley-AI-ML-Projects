# 🚗 Capstone Project: Predicting Toyota Vehicle Purchases

**Author:** Archana Rajadnya  
**Course:** UC Berkeley – AI & Machine Learning

---

### 📌 Executive Summary
This project explores customer demographic, financial, and behavioral data to predict which Toyota vehicle model a customer is most likely to purchase. By analyzing factors such as income, family size, and commuting habits, the system provides a data-driven diagnostic tool to assist dealerships. In testing, the final **Tuned CatBoost** model achieved a **96% accuracy rate**, transforming traditional inventory planning into a personalized, predictive process.

---

### 🎯 Problem Statement
Automotive dealerships often struggle with "mismatched" leads where customers are shown vehicles that do not fit their budget or daily utility needs. This leads to longer sales cycles and lower customer satisfaction.  
* **Goal:** Build a predictive engine to instantly profile customers and suggest the most compatible Toyota model.
* **Challenges:** Capturing the "hidden" logic of why a buyer chooses one segment over another.
* **Benefits:** Faster sales, optimized inventory management, and personalized marketing.

---

### ❓ Model Outcomes & Predictions
* **Learning Type:** Supervised Learning.
* **Problem Type:** Multi-Class Classification.
* **Expected Output:** Identification of the correct vehicle segment (Camry, Corolla, RAV4, Prius, Tacoma, Highlander).

---

### 📊 Data Acquisition
The dataset represents 50,000 potential buyers and includes demographic, financial, and behavioral data. Data was analyzed across multiple dimensions to ensure a clear path to solving the classification problem.

![Missing Values](./images/missing_values_per_column.png)  
*Figure 1: Visualization assessing data potential by checking for consistency and completeness.*

---

### 🧹 Data Preprocessing & Preparation
To ensure the data was model-ready, the following techniques were applied:
* **Cleaning:** Removal of duplicate records and statistical imputation were used to ensure the data was free of missing values and inconsistencies.
* **Encoding:** Categorical variables were transformed using appropriate encoding steps for machine learning compatibility.
* **Data Splitting:** The processed data was split into **Training** and **Test** sets to validate model performance on unseen data.

---

### 🔍 Exploratory Data Analysis (EDA)
EDA was conducted to identify feature distributions and relationships between variables.

![Vehicle Models Distribution](./images/vehicle_models.png)  
*Figure 2: Distribution of vehicle categories across the primary dataset.*

![Income vs Vehicle Type](./images/income_vs_vehicle_models.png)  
*Figure 3: Income distribution trends demonstrating financial separation between models.*

---

### 🤖 Modeling
The project evaluated several machine learning algorithms to address the problem statement:
* **Baseline:** Simple decision rules and Random Forest.
* **Champion Model:** **CatBoost**, selected for its superior ability to handle complex relationships between categorical and numerical features.

---

### 📈 Model Evaluation
Multiple models, including classification and tree-based algorithms, were considered.
* **Metrics:** Accuracy and **Macro F1-Score** were the primary metrics used to determine the most optimal model.
* **Results:** The Tuned CatBoost model achieved a **96% F1-Score**, showing extreme reliability in distinguishing between similar models.

![Feature Importance](./images/feature_importance.png)  
*Figure 4: Key drivers identified by the optimal model, showing the high impact of the Affordability Index.*

![Baseline Confusion Matrix](./images/confusion_matrix_baseline_model.png)  
*Figure 5: Evaluation of the baseline model performance across vehicle segments.*

---

### 🚀 Live Interface & API
The project includes a user-friendly interface and a robust API for real-world deployment.

#### **Streamlit Dashboard**
The interactive UI allows sales teams to input customer profiles and receive a "Top 3" list of recommendations.

![Toyota Matchmaker UI](./images/Toyota_Model_Matchmaker_UI.jpg)
*Figure 6: The live Streamlit application interface.*

#### **FastAPI Backend**
The backend API enables raw predictions and integration with existing dealership CRMs.

![FastAPI Documentation](./images/Toyota_Model_Matchmaker_API.jpg)
*Figure 7: The FastAPI Swagger documentation for raw model predictions.*

---

##### Contact and Further Information
**Archana Rajadnya** 
