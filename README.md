# Project 3 - Customer-churn-prediction

# Table of Content
- Overview
- Problem Statement and Motivation
- Technical Aspects
- Visualizations
- Challenges and Solutions

# 1- Overview :
The aim of this project is to perform customer churn prediction on a bank dataset. Using machine learning classification techniques, I analyzed a dataset comprising approximately 10,000 records. The dataset was sourced from Kaggle and serves as the foundation for training our customer churn classification model.

# 2- Problem Statement and Motivation :
In this project, I aimed to tackle a significant issue in the banking industry – customers leaving. This is a crucial problem because it can seriously affect a bank's revenue and financial stability. By utilizing data-driven techniques, our objective was to predict and prevent customer churn. I also recognized that churn patterns can vary based on geographical and demographic factors. Our approach was to predict churn before it occurred, enabling us to allocate resources effectively. Ultimately, our goal was to enhance customer satisfaction and retain their loyalty to the bank.


# 3- Technical Aspects :
In this project i have used python programming language and its libraries - scikit-learn,pandas, numpy,matplotlib,seaborn,xgboost for different purpose like
- Performed Explolatory data analysis using matplotlib and seaborn.
- Created new features (feature engineering) like exited,stayed for further analysis.
- Converted categorical columns to numerical using Labelencoder.
- Applied standard scalar to ensure that all the features in a dataset are on a similar scale,making it easier for machine learning models to learn and make accurate predictions,especially when features have different units or ranges.
- I tried several models like LogisticRegression , decision tree.
- Performed hyperparameter tuning and Random Forest model did the best with and accuracy of 0.86.

# 4 - Challenges and Solutions:
Challenges:
- Class Imbalance: In customer churn prediction, it's common to have an imbalanced dataset, where the number of customers who stayed far exceeds those who left.
This imbalance can lead to model bias,where the model may have difficulty in correctly identifying the minority class (churned customers).

Solutions :
-Utilized models like Random Forest (with tuned hyperparameters) that are robust and less prone to overfitting, making the model more reliable when dealing with imbalanced datasets.

  

  # 5 - Visualizations:

  ![Image](https://github.com/Karanmanolaa/Sentiment-Analysis-Of-Threads-App-Reviews-/blob/main/images/download%202.png)
  
