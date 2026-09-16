# Customer Churn Prediction

## Project Overview
Customer churn is a major challenge for businesses because losing existing customers can result in reduced revenue and increased customer acquisition costs. This project uses machine learning to identify customers who are at risk of churning and provide insights that can support proactive customer-retention strategies.

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

The dataset contains customer-level information including demographic, behavioral, and account-related variables, together with a binary churn indicator.

The target variable is:
- `Churn = 0` - Customer did not churn
- `Churn = 1` - Customer churned

## Methodology

### 1. Data Preparation

- Checked for missing values and duplicate records.
- Examined variable data types.
- Checked for the number of unique values each variable has.

### 2. Exploratory Data Analysis

Exploratory analysis was performed to investigate relationships between customer characteristics and churn.

Key areas investigated include:
- Customer demographics
- Account characteristics
- Customer tenure
- Customer behavior
- Churn rates across different customer groups

### 3.  Feature Engineering

Additional features were created from existing variables to capture potentially meaningful customer behavior and improve model performance.

Feature engineering included grouping continuous variables into meaningful categories and creating aggregated or derived customer-level features.

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

Because identifying customers who were likely to churn was the key objective, particular attention was given to **recall for the churn class**.

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

The model correctly identified **325 churners**, while **82 churners were missed**. It also identified 501 non-churning customers as potential churners.

## Business Insights

The results demonstrate how predictive analytics can support proactive customer retention.

Key business recommendations:

1. **Identify and prioritise high-risk customers early**
  Use churn probabilities to identify customers who may be at risk of leaving before they actually churn.   
2. **Develop targeted retention strategies**
  Customer characteristics and behavioral patterns can be used to personalise retention campaigns rather than applying the same strategy to every customer.

3. **Prioritise high-risk customers**
   Customers with higher predicted churn probabilities can receive higher-priority retention interventions.

4. **Balance retention costs and false positives**
   The model produces a relatively high number of false positives. The business should therefore consider the cost of contacting customers who are unlikely to churn against the potential revenue lost from failing to retain genuine churners.

## Conclusion 

This project demonstrates how machine learning can be applied to customer churn prediction to support data-driven retention strategies. The final Decision Tree achieved an AUC of 0.742 and a churn recall of approximately 81%, demonstrating  a reasonable ability to distinguish between customers who churn and those who remain.
Although the model produces a relatively high number of false positives, its strong recall makes it useful as a tool for identifying customers who may require retention attention. Further optimisation of probability thresholds and feature engineering could improve precision while maintaining an appropriate level of churn detection.
The project highlights the value of combining **exploratory data analysis, feature engineering, machine learning, and business interpretation** to address a real-world customer analytics problem.

## Technologies Used 

- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- SQL Server Management Studio
- Power BI
- Streamlit
- Comet 

```markdown
## Live Demo

Try the deployed customer churn prediction application:
https://churnprediction-9yookwlzdpasakhcx4erhd.streamlit.app/

## Streamlit App
<img width="566" height="590" alt="image" src="https://github.com/user-attachments/assets/4b95cc28-c490-4d94-bc13-6e432bd743f5" />
```
A
