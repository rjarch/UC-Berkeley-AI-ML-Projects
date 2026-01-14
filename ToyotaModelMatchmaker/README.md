# 🚗 Toyota Model Matchmaker: AI-Driven Customer Profiling

#### Executive Summary
The **Toyota Model Matchmaker** is a machine learning-powered system designed to predict the most suitable vehicle for a potential customer based on their unique lifestyle and financial profile. By evolving through three strategic phases—Baseline, Strategic Rebalancing, and Behavioral Feature Engineering—the system successfully resolved majority-class bias to identify niche buyers.

In testing, the final **Tuned CatBoost** model achieved a **96% accuracy rate** and a **96% Macro F1-Score**, transforming the traditional "guessing game" of sales into a surgical, data-driven diagnostic tool.

---

### **1. Problem Statement**
Automotive dealerships often struggle with "mismatched" leads—where customers are shown vehicles that don't fit their budget or daily utility needs. This leads to longer sales cycles and lower customer satisfaction.

**Our Goal:** To build a predictive engine that can instantly profile a customer and suggest the most compatible Toyota model.
* **Challenges:** Capturing the "hidden" logic of why someone chooses a niche model (like a Tacoma or Prius) over a high-volume SUV (like a RAV4).
* **Benefits:** Faster sales cycles, optimized inventory management, and personalized marketing.

---

### **2. The Data (Our Ingredients)**
We used a dataset representing 50,000 potential buyers. To make the model smarter, we moved beyond raw data to create **Behavioral Proxies**:

* **Affordability Index:** A calculated ratio of income to vehicle cost.
* **Utility Scores:** Combining family size and commute distance to see if a user *actually* needs an SUV.
* **Lifestyle Indicators:** Mapping "Urban" vs. "Rural" living to specific vehicle categories (e.g., trucks for rural, hybrids for urban).

---

### **3. Methodology (How it Works)**
We approached this as a **Supervised Classification** problem, comparing three distinct architectures to find the "Gold Standard" solution.

1.  **Exploration:** We identified that income and family size were the strongest predictors of vehicle choice.
2.  **Strategic Rebalancing:** We intentionally addressed class imbalance to ensure niche models (Tacoma, Prius) received equal predictive weight.
3.  **Model Selection:** We compared multiple "AI experts" (algorithms):
    * **Baseline:** Random Forest (88% Accuracy, but biased toward majority classes).
    * **Advanced:** **CatBoost (Champion)**, which achieved elite precision by handling categorical interaction features natively.

---

### **4. Results & Findings**

#### **🏆 Final Model Tournament Results**
| Metric | Random Forest (Baseline) | XGBoost (Final) | **CatBoost (Tuned Champion)** |
| :--- | :---: | :---: | :---: |
| **Global Accuracy** | 88.00% | 96.00% | **96.00%** |
| **Macro F1-Score** | 0.87 | 0.96 | **0.96** |
| **Tacoma Precision** | 0.95 | 0.98 | **1.00 (Perfect)** |
| **Highlander F1-Score**| 0.94 | 0.97 | **0.98** |

* **High Precision:** The model reached a **96% F1-Score**, meaning it is extremely reliable at distinguishing between similar models.

    ![Confusion Matrix](./images/confusion_matrix.png)
    *Figure 1: Confusion Matrix showing the high accuracy of predictions across all vehicle models.*

* **Key Drivers:** We discovered that our engineered **Affordability Index** and **SUV Affinity** scores were significantly more important than age or simple occupation when predicting a purchase.

    ![Feature Importance](./images/catboost_feature_importance.png)
    *Figure 2: This plot illustrates the dominance of engineered behavioral signals over raw demographic data.*

* **The "Top-K" Strategy:** Instead of giving just one answer, the system provides the **Top 3** choices. This mimics a real conversation with a sales expert, offering options while staying within the user's "compatibility zone."

---

### **5. Next Steps & Recommendations**
To take this from a Capstone project to a real-world dealership tool, we recommend:
1.  **Integration with CRM:** Connect this tool to dealership websites so customers can "Find their Match" before walking onto the lot.
2.  **Real-Time Inventory Sync:** Link the model to current stock. If the #1 choice is out of stock, the system should automatically pivot to the #2 choice.
3.  **Customer Feedback Loop:** Use real sales outcomes to "retrain" the model every month, allowing it to adapt to changing market trends.

---

### **6. How to Run the Project**
For technical reviewers who wish to test the live application:

1.  **The Live Interface (Streamlit):**
    * Start the UI by running `streamlit run app.py` in your terminal.
    * Access it via your web browser, typically at `http://localhost:8501`.

    ![Streamlit UI](./images/sample_prediction_ui.png)
    *Figure 4: The interactive Streamlit dashboard where users receive recommendations.*

2.  **The API Backend (FastAPI):**
    * Ensure the backend is running by executing `python main.py` in a separate terminal.
    * Access the interactive API documentation at `http://127.0.0.1:8000/docs`.

---
