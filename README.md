# Customer Churn Prediction

## Project Overview
Customer churn is a major challenge for businesses because losing existing customers can result in reduced revenue and increased customer aquisition costs. This project uses machine learning to identify customers who are at risk of churning and provide insights that can support proactive customer-retention strategies.

This project explores customer demographics, account characteristics, and behavioral patterns to determine factors associated with churn and develop a predictive classification model.

## Objectives 
The main objectives of this project were to:

- Explore customer characteristics and identify patterns associated with churn.
- Perform data cleaning and exploratory data analysis (EDA).
- Engineer relevant features to improve predictive performance.
- Train and compare multiple classification models.
- Tune model hyperparameters using cross-validation.
- Evaluate models using precision, recall, and F1-score, confusion matrices, and ROC-AUC.
- Identify customers who are potentially at high risk of churn.
- Translate model results into actionable business recommendations.

## Dataset

The dataset contains customer-level information including demographic, behavioral, and account-related variables, together with a binary churn indicatior.

The target variable is:
- `Churn = 0` - Customer did not churn
- `Churn = 1` - Customer churned

## Methodology

### 1. Data Preparation

- Checked for missing values and duplicate records.
- Examined variable data types.
- Checked for the number of unique values each varible has.

### 2. Exploratory Data Analysis

Exploratory analysis was performed to investigate relationships between customer characteristics and churn.

Key areas investigated include:
- Customer demographics
- Account characteristics
- Customer tunure
- Customer behavior
- Churn rates acros different customer groups

### 3.  Feature Engineering

Additional features were created from existing variables to capture potential meaningful customer bahavior and improve model performance.

Feature engineering included grouping continous variables into meaningful categories and creating aggregated or derived customer-level features.

### 4. Model Development

Several classification algorithms were evaluated, including:

- Logistic regression
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)

Hyperparameter tuning and cross-validation were used to improve model performance and reduce overfitting.

### 5. Model Evaluation

Models were evaluated using:

- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC

Because identifying customers who were likely to churn was the key objective, particila attention was given to **recall for the churn class**.

## Results

The Decision Tree classifier achieved a ROC-AUC of **0.742**, indicating acceptable discriminatory ability.

At the selected operating point, the model achieved approximately:
- **Recall: 79.9%**
- **Precision: 39.3%**
- **F1-score: 53%**
- **Accuracy: 70%**
- **False Positive Rate: ~ 31.5%**

The model successfully identified approximately 80% of customers who actually churned. However, the relatively low precision indicates that a significant number of customers were incorrectly classified as potential churners.

## Confusion Matrix

The final Decision Tree produced the following results:

| | Predicted No Churn | Predicted Churn |
|---|---:|---:|
| **Actual No Churn** | 1,092 | 501 |
| **Actual Churn** | 82 | 325 |

## Streanlit App
<img width="566" height="590" alt="image" src="https://github.com/user-attachments/assets/4b95cc28-c490-4d94-bc13-6e432bd743f5" />
