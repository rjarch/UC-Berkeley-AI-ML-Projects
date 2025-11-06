# 📈 Practical Application III: Comparing Classifiers

## Overview
This repository contains the solution for Practical Application III, an assignment for a UC Berkeley data science or machine learning course. The primary objective of this project was to **compare the performance of various classification models** on a real-world marketing dataset.

The following classifiers were implemented and evaluated:
* **K-Nearest Neighbors (KNN)**
* **Logistic Regression**
* **Decision Tree**
* **Support Vector Machine (SVC)**

---

## 🎯 Project Goal
The core goal was to predict whether a customer would subscribe to a term deposit (the target variable 'y') after being contacted during a telephone marketing campaign. We systematically evaluated each model's performance using metrics like **accuracy, recall, precision, and F1-score**, both with default and optimized hyperparameters.

---

## 📂 Data Source and Description

### Dataset
The project utilizes the **Bank Marketing Data Set** from the UCI Machine Learning Repository.

* **Source:** [UCI Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
* **Target Variable:** `y` (Whether the client subscribed to a term deposit - 'yes' or 'no').
* **Context:** The data represents the results of **4 marketing campaigns** performed by a Portuguese banking institution (as indicated in the accompanying research paper).

### Preprocessing
The dataset required standard preprocessing steps, including:
1.  **Feature Encoding:** Handling categorical variables (e.g., one-hot encoding).
2.  **Feature Scaling:** Standardizing numerical features to prevent models like KNN and SVC from being dominated by features with large scales.
3.  **Handling Imbalance:** The target variable is inherently imbalanced, which was considered when evaluating models (prioritizing metrics like F1-score and Recall).

---

## ⚙️ Methodology

The comparison was performed in two main phases:

### Phase 1: Default Parameters
All four classifiers were trained and evaluated using their **default hyperparameters** in `scikit-learn`. This provided a baseline for their inherent performance on the dataset.

* **Visualization:** **Model_comparison_default_parameters.png** and **Improved_Model_comparison_default_parameters.png** show the comparative performance metrics (accuracy, etc.) for the default models.

### Phase 2: Hyperparameter Tuning
We then utilized techniques like **GridSearchCV** or **RandomizedSearchCV** to find the optimal hyperparameters for each model, aiming to maximize performance, particularly the F1-score due to the imbalanced nature of the data.

* **Visualization:** **Model_performance_comparison.png** shows the final, tuned performance metrics.

---

## 📊 Key Results and Findings

### Best Performing Models (Tuned)

| Model | Key Metric (F1-Score) | Notes |
| :--- | :--- | :--- |
| **Logistic Regression** | **[Highest F1-Score]** | Excellent balance of performance and speed. |
| **SVC** | [Second Highest F1-Score] | High accuracy but computationally expensive when tuned. |

### Performance Visualizations

| Image File | Description |
| :--- | :--- |
| `Model_performance_comparison.png` | Comparison of all four models after **hyperparameter tuning**. This shows the final performance metrics (Accuracy, F1-Score, Recall, Precision). |
| `confusion_matrix_logistic_regression.png` | The confusion matrix for the final **Logistic Regression** model. This highlights its ability to identify True Positives (subscribers) and True Negatives (non-subscribers). |
| `Model_comparison_default_parameters.png` | Initial comparison of models using **default settings**. |

### Conclusion from Notebook Snippet
> - **Most Accurate:** SVC (Tuned)
> - **Most Expensive:** SVC (Tuned)
> - **Recommended Models:** For a medium-sized dataset, **Logistic Regression** and **Decision Tree** offer the best balance between accuracy, interpretability, and computational cost.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x
* The following libraries:
    * `pandas`
    * `numpy`
    * `scikit-learn`
    * `matplotlib` or `seaborn`

### Files in Repository
* `prompt_III.ipynb`: The main Jupyter Notebook containing all the code for data loading, preprocessing, model training, tuning, and evaluation.
* `Model_performance_comparison.png`: Final comparison plot of tuned models.
* `confusion_matrix_logistic_regression.png`: Confusion Matrix for the best performing practical model.
* *(Other image files)*: Supporting plots and visualizations from the analysis phase.

To run the analysis:
1.  Clone this repository.
2.  Ensure all prerequisites are installed (`pip install -r requirements.txt` if a `requirements.txt` file is included, otherwise install manually).
3.  Open and run the cells in `prompt_III.ipynb`.

---
